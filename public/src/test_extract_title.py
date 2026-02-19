import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = """# My Title """
        title = extract_title(markdown)
        self.assertEqual(title, "My Title")

    def test_extract_title_no_title(self):
        markdown = """This is some markdown without a title."""
        with self.assertRaises(ValueError):
            extract_title(markdown)

if __name__ == '__main__':
    unittest.main()