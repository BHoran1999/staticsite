import re
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    
    new_nodes = []

    if old_nodes is None:
        return new_nodes
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        matches = re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", old_node.text)

        if not matches:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text

        for alt_text, url in matches:
            image_markdown = f"![{alt_text}]({url})"
            segments = remaining_text.split(image_markdown, 1)

            if segments[0]:
                new_nodes.append(TextNode(segments[0], TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            remaining_text = segments[1] if len(segments) > 1 else ""
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    if old_nodes is None:
        return new_nodes
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        matches = re.findall(r"\[([^\]]*)\]\(([^)]+)\)", old_node.text)

        if not matches:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text

        for link_text, url in matches:
            link_markdown = f"[{link_text}]({url})"
            segments = remaining_text.split(link_markdown, 1)

            if segments[0]:
                new_nodes.append(TextNode(segments[0], TextType.TEXT))

            new_nodes.append(TextNode(link_text, TextType.LINK, url))
            remaining_text = segments[1] if len(segments) > 1 else ""
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes