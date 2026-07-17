import json
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))

from search_images import search_images


class FakeResponse:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self):
        return json.dumps(
            {
                "images": [
                    {
                        "title": "Official statement",
                        "imageUrl": "https://example.com/official.jpg",
                        "thumbnailUrl": "https://example.com/thumb.jpg",
                        "source": "Official site",
                        "link": "https://example.com/statement",
                        "imageWidth": 1200,
                        "imageHeight": 800,
                    },
                    {
                        "title": "Duplicate",
                        "imageUrl": "https://example.com/official.jpg",
                    },
                ]
            }
        ).encode()


class SearchImagesTest(unittest.TestCase):
    def test_posts_localized_query_and_normalizes_unique_results(self):
        captured = {}

        def opener(request, timeout):
            captured["request"] = request
            captured["timeout"] = timeout
            return FakeResponse()

        results = search_images(
            "香港愛護動物協會 虐狗影片 下架 聲明",
            api_key="test-key",
            limit=5,
            opener=opener,
        )

        request = captured["request"]
        self.assertEqual(request.full_url, "https://google.serper.dev/images")
        self.assertEqual(request.method, "POST")
        self.assertEqual(captured["timeout"], 30)
        self.assertEqual(
            json.loads(request.data),
            {
                "q": "香港愛護動物協會 虐狗影片 下架 聲明",
                "gl": "hk",
                "hl": "zh-tw",
            },
        )
        self.assertEqual(request.headers["X-api-key"], "test-key")
        self.assertEqual(
            results,
            [
                {
                    "rank": 1,
                    "title": "Official statement",
                    "image_url": "https://example.com/official.jpg",
                    "thumbnail_url": "https://example.com/thumb.jpg",
                    "source": "Official site",
                    "source_url": "https://example.com/statement",
                    "width": 1200,
                    "height": 800,
                }
            ],
        )


if __name__ == "__main__":
    unittest.main()
