from markdown_blocks import markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode, ParentNode, LeafNode
from split_nodes import text_to_textnodes
from textnode import TextNode, text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "paragraph":
            html_nodes.append(create_paragraph_node(block))
        elif block_type == "heading":
            level = determine_header_level(block)
            html_nodes.append(create_header_node(block, level))
        elif block_type == "code":
            html_nodes.append(create_code_node(block))
        elif block_type == "ordered_list":
            html_nodes.append(create_ordered_list_node(block))
        elif block_type == "unordered_list":
            html_nodes.append(create_unordered_list_node(block))
        elif block_type == "quote":
            html_nodes.append(create_quote_node(block))

        

    return ParentNode(html_nodes, "div")

def create_paragraph_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode(children, "p")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def determine_header_level(block):
    level = 0
    for char in block:
        if char == '#':
            level += 1
        elif char == ' ':
            break
    return level

def create_header_node(block, level):
    content = block.lstrip("#").strip()

    children = text_to_children(content)
    return ParentNode(children, f"h{level}")

def create_code_node(block):
    text = block[4:-3]
    text_node = TextNode(text, "code")
    html_node = text_node_to_html_node(text_node) 
    return html_node

def create_ordered_list_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode(children, "li"))
    return ParentNode(html_items, "ol")

def create_unordered_list_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode(children, "li"))
    return ParentNode(html_items, "ul")

def create_quote_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode(children, "blockquote")