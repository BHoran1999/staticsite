import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_no_match(self):
        matches = extract_markdown_images(
            "This is text with no images"
        )
        self.assertListEqual([], matches)


    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com)"
        )
        self.assertListEqual([("link", "https://www.google.com")], matches)

    def test_extract_multiple_links(self):
        text = "[first](url1.com) and [second](url2.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("first", "url1.com"), ("second", "url2.com")], matches)

    def test_extract_markdown_links_no_match(self):
        matches = extract_markdown_links(
            "This is text with no links"
        )
        self.assertListEqual([], matches)

if __name__ == "__main__":
    unittest.main()