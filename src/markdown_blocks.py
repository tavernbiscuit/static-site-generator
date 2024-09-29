def block_to_block_type(block):
    block_type = "paragraph"
    for i in range(1, 7):
        if block.startswith("#" * i + " "):
            block_type = "heading"
    if block.startswith("```") and block.endswith("```"):
        block_type = "code"
    if block.startswith(">"):
        is_quote = True
        lines = block.split("\n")
        for line in lines:
           if not line.startswith(">"):
               is_quote = False
               break
        if is_quote:
            block_type = "quote"
    if block.startswith("* ") or block.startswith("- "):
        is_unordered_list = True
        lines = block.split("\n")
        for line in lines:
           if not (line.startswith("* ") or line.startswith("- ")):
               is_unordered_list = False
               break
        if is_unordered_list:
            block_type = "unordered_list"
    if block.startswith("1. "):
        i = 1
        is_ordered_list = True
        lines = block.split("\n")
        for line in lines:
            if line.startswith(f"{i}."):
                i += 1
                continue
            else:
                is_ordered_list = False
        if is_ordered_list:
            block_type = "ordered_list"
    
    
    return block_type

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    processed_blocks = []
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block:
            processed_blocks.append(stripped_block)

    return processed_blocks
    