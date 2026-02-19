from textnode import TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node):

    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)

    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)

    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text) 

    if text_node.text_type == TextType.LINK:
        node = LeafNode("a", text_node.text, {"href": text_node.url})
        html = node.to_html()
        print(f"DEBUG LINK: text='{text_node.text}', url='{text_node.url}'")
        print(f"DEBUG LINK: props={node.props}")
        print(f"DEBUG LINK: props_to_html()='{node.props_to_html()}'")
        print(f"DEBUG LINK: Generated HTML: '{html}'")
        return node
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    raise ValueError(f"Unsupported text type: {text_node.text_type}")
