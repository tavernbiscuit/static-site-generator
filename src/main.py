from textnode import TextNode, text_type_text
from split_nodes import text_to_textnodes

def main():
    text = "This is **bold** and *italic* text."
    result = text_to_textnodes(text)
    print(result)

main()