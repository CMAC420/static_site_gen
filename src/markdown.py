from src.block_type import BlockType, block_to_block_type
from src.blocks import markdown_to_blocks
from text import text_to_text_node
from textnode import text_node_to_html_node
from htmlnode import ParentNode, LeafNode

def text_to_children(text):
    text_node = text_to_text_node(text)
    return [text_node_to_html_node(node) for node in text_node]

def paragraph_to_html(block):
    return ParentNode("p", text_to_children(block))

def heading_to_html(block):
    level = len(block) - len(block.strip("#"))
    text = block[level + 1:]
    return ParentNode(f"h{level}", text_to_children(text))

def code_to_html(block):
    text = block.strip("`").strip()
    code_node = LeafNode(None, text)
    return ParentNode("pre", [ParentNode("code", [code_node])])

def quote_to_html(block):
    lines = block.split("\n")
    cleaned = "\n".join(line[1:].lstrip for line in lines)
    return ParentNode("blockquote", text_to_children(cleaned))

def unordered_list_to_html(block):
    items = []
    for line in block.split("\n"):
        text = line.split(". ", 1)[1]
        items.append(ParentNode("li", text_to_children(text)))
    return ParentNode("ul", items)

def ordered_list_to_html(block):
    items = []
    for line in block.split("\n"):
        text = line.split(". ", 1)[1]
        items.append(ParentNode("li", text_to_children(text)))
    return ParentNode("ol", items)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            children.append(paragraph_to_html(block))
        if block_type == BlockType.HEADING:
            children.append(heading_to_html(block))
        if block_type == BlockType.CODE:
            children.append(code_to_html(block))
        if block_type == BlockType.QUOTE:
            children.append(quote_to_html(block))
        if block_type == BlockType.UNORDERED_LIST:
            children.append(unordered_list_to_html(block))
        if block_type == BlockType.ORDERED_LIST:
            children.append(ordered_list_to_html(block))

    return ParentNode("div", children)

