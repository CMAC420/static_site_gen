from src.textnode import TextType, TextNode
from src.extract_markdown import extract_markdown_images, extract_markdown_links

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

def split_node_image(old_node):
    new_node = []
    for node in old_node:
        if node.text_type != TextType.TEXT:
            new_node.append(node)
            continue
        
        text = node.text
        image = extract_markdown_images(text)

        if not image:
            new_node.append(node)
            continue

        for alt, url in image:
            image_markdown = f"![{alt}]({url})"
            before, after = text.split(image_markdown, 1)

            if before:
                new_node.append(TextNode(before, TextType.TEXT))
            new_node.append(TextNode(alt, TextType.IMAGE, url))

            text = after

        if text:
            new_node.append(TextNode(text, TextType.TEXT))
    return new_node

def split_node_link(old_node):
    new_node = []

    for node in old_node:
        if node.text_type != TextType.TEXT:
            new_node.append(node)
            continue
        
        text = node.text
        link = extract_markdown_links(text)

        if not link:
            new_node.append(node)
            continue

        for anchor, url in link:
            link_markdown = f"[{anchor}]({url})"
            before, after = text.split(link_markdown, 1)

            if before:
                new_node.append(TextNode(before, TextType.TEXT))
            new_node.append(TextNode(anchor, TextType.LINK, url))

            text = after

        if text:
            new_node.append(TextNode(text, TextType.TEXT))

    return new_node