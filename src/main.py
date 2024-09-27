from textnode import *
from htmlnode import*
from split_nodes import *

def main():
    node = TextNode(
    "This is text with an image ![alt text](https://example.com/image.jpg) and another ![second](https://example.com/second.jpg)",
    text_type_text
)
    result = split_nodes_image([node])
    print(result)

main()