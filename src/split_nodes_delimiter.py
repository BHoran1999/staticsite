from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for old_node in old_nodes:    
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        segments = old_node.text.split(delimiter)
    
        if len(segments) % 2 == 0:
            raise ValueError(f"Invalid markdown: unmatched delimiter '{delimiter}'")

        for i, segment in enumerate(segments): 

            if segment == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(segment, TextType.TEXT))

            else:
                new_nodes.append(TextNode(segment, text_type))

    return new_nodes

        