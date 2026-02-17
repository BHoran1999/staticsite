from textnode import TextNode, TextType
from htmlnode import LeafNode
from text_node_to_html_node import text_node_to_html_node
import unittest


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("Plain text", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Plain text")

if __name__ == "__main__":
    unittest.main()
