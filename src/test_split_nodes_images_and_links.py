import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from split_nodes_images_and_links import split_nodes_image, split_nodes_links

class TestSplitNodesImagesAndLinks(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_multiple_images(self):
        node = TextNode(
            "![first image](url1.com) and ![second image](url2.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            [
                TextNode("first image", TextType.IMAGE, "url1.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "url2.com"),
            ],
            new_nodes,
        )

    def test_split_links(self):

        node = TextNode(
            "This is text with an [link](https://www.google.com) and another [second link](https://www.facebook.com)",
            TextType.TEXT
        )

        new_nodes = split_nodes_links([node])

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://www.facebook.com"
                ),
            ],
            new_nodes,
        )



if __name__ == "__main__":
    unittest.main()