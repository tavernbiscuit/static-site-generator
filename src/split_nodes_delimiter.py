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

