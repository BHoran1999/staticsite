import re

def markdown_to_blocks(markdown):
    if markdown is None:
        return []
    
    blocks = markdown.split("\n\n")
    
    blocks_list = []

    for block in blocks:
        block = block.strip()
        if block == "":
            continue

        blocks_list.append(block)

    return blocks_list

