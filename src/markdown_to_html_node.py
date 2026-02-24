from blocktype import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_node_to_html_node import text_node_to_html_node
from text_to_textnodes import text_to_textnodes

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

def markdown_to_html_node(markdown):
    
    blocks = markdown_to_blocks(markdown)
    
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.HEADING:
            level = 0
            for char in block:
                if char == "#":
                    level += 1
                else:
                    break
            text = block[level + 1:]
            node = ParentNode(f"h{level}", text_to_children(text))

        elif block_type == BlockType.CODE:
            code = block[4:-3]
            code_node = ParentNode("code", text_to_children(code))
            node = ParentNode("pre", [code_node])

        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            items = []
            for line in lines:
                if line.startswith("> "):
                    items.append(line[2:])
                elif line.startswith(">"):
                    items.append(line[1:])
            quote = "\n".join(items)
            node = ParentNode("blockquote", text_to_children(quote))

        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            items = []
            for line in lines:
                item = line[2:]
                items.append(ParentNode("li", text_to_children(item)))
            node = ParentNode("ul", items)

        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            items = []
            for i, line in enumerate(lines):
                item = line[len(f"{i + 1}. "):]
                items.append(ParentNode("li", text_to_children(item)))
            node = ParentNode("ol", items)

        else:
            lines = block.split("\n")
            text = " ".join(line.strip() for line in lines)
            node = ParentNode("p", text_to_children(text))

        children.append(node)

    return ParentNode("div", children)


    