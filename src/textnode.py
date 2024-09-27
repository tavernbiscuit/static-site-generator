from htmlnode import *
import re

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(text_node.text, None, None)
    if text_node.text_type == text_type_bold:
        return LeafNode(text_node.text, "b", None)
    if text_node.text_type == text_type_italic:
        return LeafNode(text_node.text, "i", None)
    if text_node.text_type == text_type_code:
        return LeafNode(text_node.text, "code", None)
    if text_node.text_type == text_type_link:
        return LeafNode(text_node.text, "a", {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode(
            "", "img", {"src": text_node.url, "alt": text_node.text}
        )
    raise Exception("Invalid TextNode type.")

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if (
            self.text == other.text and self.text_type == other.text_type
        and self.url == other.url
        ):
            return True
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"