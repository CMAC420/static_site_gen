from src.splitnode import split_node_delimiter, split_node_link, split_node_image
from src.textnode import TextNode, TextType

def text_to_text_node(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_node_image(nodes)
    nodes = split_node_link(nodes)
    nodes = split_node_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_node_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_node_delimiter(nodes, "`", TextType.CODE)

    return nodes