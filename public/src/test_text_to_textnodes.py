import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):

    def test_simple_text(self):
        text = "This is a simple text."
        result = text_to_textnodes(text)
        expected = [TextNode(text, TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_bold_text(self):
        text = "This is **bold** text."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_italic_text(self):
        text = "This is *italic* text."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_code_text(self):
        text = "This is `code` text."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text.", TextType.TEXT)
        ]
        self.assertEqual(result, expected)