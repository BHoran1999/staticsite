from textnode import TextNode, TextType
from text_node_to_html_node import text_node_to_html_node

def main():
    text_node = TextNode("This is some bold text", TextType.BOLD)
    html_node = text_node_to_html_node(text_node)

    print(self.assertEqual(html_node.tag, None))
    self.assertEqual(html_node.value, "This is some bold text")

main()