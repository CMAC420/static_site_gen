def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    
    blocks = []
    for block in raw_blocks:
        stripped = block.strip()
        if stripped:
            blocks.append(stripped)
    return blocks

def extract_title(markdown):
    for line in markdown.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No header available")