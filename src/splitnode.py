from src.textnode import *

def split_node_delimiter(old_node, delimiter, text_type):
    new_node = []
    
    for node in old_node:
        if node.text_type != TextType.TEXT:
            new_node.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts)%2==0:
            raise ValueError(f"Invalid markdown delimiter '{delimiter}' int text: {node.text}")
        
        for i, part in enumerate(parts):
            if part == "":
                continue

            if i % 2 == 0:
                new_node.append(TextNode(part, TextType.TEXT))

            else:
                new_node.append(TextNode(part, text_type))

    return new_node