from textnode import *

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)

        else:
            node_split = node.text.split(delimiter)
            if len(node_split) % 2 == 0:
                raise ValueError("Invalid Markdown syntax.")
            
            processed_nodes = []
            for i in range(len(node_split)):
                part = node_split[i]
                if part:
                    if i % 2 == 0:
                        processed_nodes.append(TextNode(part, text_type_text))
                    else:
                        processed_nodes.append(TextNode(part, text_type))

            new_nodes.extend(processed_nodes)
    
    return new_nodes

#Markdown parsing utility functions

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches

#Splitting nodes using Markdown parsing utility functions

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        text = node.text
        matches = extract_markdown_links(node.text)

        if not matches:
            new_nodes.append(node)
            continue
    
        for match in matches:
            link_text, url = match
            parts = text.split(f"[{link_text}]({url})", 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], text_type_text))
            new_text_node = TextNode(link_text, text_type_link, url)
            new_nodes.append(new_text_node)
            text = parts[1] if len(parts) > 1 else ""

        if text:
            new_nodes.append(TextNode(text, text_type_text))

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        text = node.text
        matches = extract_markdown_images(node.text)

        if not matches:
            new_nodes.append(node)
            continue
    
        for match in matches:
            alt_text, url = match
            parts = text.split(f"![{alt_text}]({url})", 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], text_type_text))
            new_text_node = TextNode(alt_text, text_type_image, url)
            new_nodes.append(new_text_node)
            text = parts[1] if len(parts) > 1 else ""

        if text:
            new_nodes.append(TextNode(text, text_type_text))

    return new_nodes
    