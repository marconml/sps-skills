#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const { pathToFileURL } = require("url");
const { chromium } = require("playwright");

async function main() {
  const report = process.argv[2];
  const outputDir = process.argv[3];
  if (!report || !outputDir) {
    throw new Error("Usage: browser_qa.js REPORT.html OUTPUT_DIR");
  }
  fs.mkdirSync(outputDir, { recursive: true });
  const options = { headless: true };
  const configured = process.env.CHROME_EXECUTABLE;
  const macChrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
  if (configured) options.executablePath = configured;
  else if (fs.existsSync(macChrome)) options.executablePath = macChrome;
  const browser = await chromium.launch(options);

  async function inspect(viewport, label, language) {
    const page = await browser.newPage({ viewport, deviceScaleFactor: 1 });
    const errors = [];
    page.on("pageerror", (error) => errors.push(String(error)));
    await page.goto(pathToFileURL(path.resolve(report)).href, { waitUntil: "load" });
    if (language === "zh") await page.click('[data-lang-option="zh"]');
    const result = await page.evaluate(() => {
      const overflow = [...document.querySelectorAll("body *")]
        .filter((element) => {
          const style = getComputedStyle(element);
          return element instanceof HTMLElement
            && element.scrollWidth > element.clientWidth + 2
            && style.overflowX === "visible";
        })
        .slice(0, 20)
        .map((element) => ({
          tag: element.tagName,
          className: String(element.className),
          clientWidth: element.clientWidth,
          scrollWidth: element.scrollWidth,
        }));
      const images = [...document.querySelectorAll("img")].map((image) => ({
        alt: image.alt,
        width: image.naturalWidth,
        height: image.naturalHeight,
        objectFit: getComputedStyle(image).objectFit,
      }));
      const evidenceLayout = [...document.querySelectorAll(".surgery-card,.evidence,.case-post")].map((card) => {
        const image = card.querySelector("img");
        const media = image?.closest("a,.evidence-media,.case-image");
        const content = card.querySelector(".surgery-body,.evidence-body,.case-post-body");
        if (!image || !media) return { hasImage: false, imageInsideMedia: true, mediaClearOfContent: true };
        const imageBox = image.getBoundingClientRect();
        const mediaBox = media.getBoundingClientRect();
        const contentBox = content?.getBoundingClientRect();
        const tolerance = 1;
        return {
          hasImage: true,
          imageInsideMedia: imageBox.left >= mediaBox.left - tolerance
            && imageBox.right <= mediaBox.right + tolerance
            && imageBox.top >= mediaBox.top - tolerance
            && imageBox.bottom <= mediaBox.bottom + tolerance,
          mediaClearOfContent: !contentBox || mediaBox.bottom <= contentBox.top + tolerance
            || mediaBox.right <= contentBox.left + tolerance,
        };
      });
      const bodySizes = [...document.querySelectorAll(".section-lead,.card p,.evidence-body p,.action p")]
        .map((element) => parseFloat(getComputedStyle(element).fontSize));
      return {
        documentWidth: [document.documentElement.clientWidth, document.documentElement.scrollWidth],
        overflow,
        images,
        evidenceLayout,
        bodySizes,
        languageState: {
          documentLanguage: document.documentElement.lang,
          defaultLanguage: document.body.dataset.defaultLanguage || "",
          activeOption: document.querySelector('[data-lang-option].active')?.dataset.langOption || "",
          h1Text: document.querySelector("h1")?.textContent.trim() || "",
        },
      };
    });
    await page.screenshot({ path: path.join(outputDir, `${label}.png`), fullPage: true });
    await page.close();
    return { viewport, errors, ...result };
  }

  const desktopEnglish = await inspect({ width: 1440, height: 1000 }, "desktop-en", "en");
  const desktopChinese = await inspect({ width: 1440, height: 1000 }, "desktop-zh", "zh");
  const mobileEnglish = await inspect({ width: 390, height: 844 }, "mobile-en", "en");
  const mobileChinese = await inspect({ width: 390, height: 844 }, "mobile-zh", "zh");
  await browser.close();
  const views = [desktopEnglish, desktopChinese, mobileEnglish, mobileChinese];
  const passed = views.every((view) =>
    view.documentWidth[0] === view.documentWidth[1]
    && view.overflow.length === 0
    && view.errors.length === 0
    && view.images.every((image) => image.width > 0 && image.height > 0 && image.objectFit === "contain")
    && view.evidenceLayout.every((item) => item.imageInsideMedia && item.mediaClearOfContent)
    && view.bodySizes.every((size) => size >= 13)
  )
    && desktopEnglish.languageState.defaultLanguage === "en"
    && desktopEnglish.languageState.activeOption === "en"
    && desktopEnglish.languageState.documentLanguage === "en"
    && desktopChinese.languageState.activeOption === "zh"
    && desktopChinese.languageState.documentLanguage === "zh-Hant"
    && desktopEnglish.languageState.h1Text !== desktopChinese.languageState.h1Text
    && mobileEnglish.languageState.h1Text !== mobileChinese.languageState.h1Text;
  const receipt = {
    status: passed ? "PASS" : "FAIL",
    report: path.resolve(report),
    desktopEnglish,
    desktopChinese,
    mobileEnglish,
    mobileChinese,
  };
  fs.writeFileSync(path.join(outputDir, "browser-qa.json"), JSON.stringify(receipt, null, 2));
  console.log(JSON.stringify(receipt, null, 2));
  process.exit(passed ? 0 : 1);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
