from textnode import *
from htmlnode import*
from split_nodes_delimiter import *

def main():
    text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))

main()