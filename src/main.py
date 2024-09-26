from textnode import *
from htmlnode import*

def main():
    htmlnode1 = (
        HTMLNode(
            None, "This is sample text", None, 
            {"href": "https://www.google.com", "target": "_blank"}
            )
    )
    print(htmlnode1.props_to_html())

main()