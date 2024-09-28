from textnode import TextNode, text_type_text
from markdown_blocks import markdown_to_blocks

def main():
    text = ("# This is a heading"
            "\n\n"
            "This is a paragraph of text. It has some **bold** "
            "and *italic* words inside of it."
            "\n\n"
            "* This is the first list item in a list block"
            "* This is a list item"
            "* This is another list item")
    result = markdown_to_blocks(text)
    print(result)

main()