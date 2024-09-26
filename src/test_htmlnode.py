import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p","This is sample text")
        node2 = HTMLNode("p","This is sample text")
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(
            "p","This is sample text", 
            None, {"href": "https://www.google.com", "target": "_blank"}
        )
        
        self.assertEqual(
            HTMLNode.props_to_html(node), 
            " href='https://www.google.com' target='_blank'"
        )

    def test_not_eq(self):
        node = HTMLNode(
            "p","This is sample text", 
            None, {"href": "https://www.google.com", "target": "_blank"}
        )
        node2 = HTMLNode(
            "h1","This is sample text", 
            None, {"href": "https://www.google.com", "target": "_blank"}
        )

    def test_children_is_none(self):
        node = HTMLNode("p", "This is sampel paragraph text", None, None)
        self.assertIsNone(node.children)

    def test_props_is_none(self):
        node = HTMLNode("p", "This is sampel paragraph text", None, None)
        self.assertIsNone(node.props)

    def test_all_are_none(self):
        node = HTMLNode()
        (self.assertIsNone(node.tag) and self.assertIsNone(node.value) 
         and self.assertIsNone(node.children) and self.assertIsNone(node.props)
    )
if __name__ == "__main__":
    unittest.main()