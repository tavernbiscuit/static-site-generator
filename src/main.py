from markdown_to_html import markdown_to_html_node

def main():
    md = """
# this is an h1

this is paragraph text

## this is an h2
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    print(html)

main()