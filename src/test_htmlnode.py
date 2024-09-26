import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    # Order
    # Tag, Value, Children, Props
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
        
class TestParentNode(unittest.TestCase):
    # Order
    # Children, Tag, Props
    def test_no_tag(self):
        node1 = LeafNode("This is sample text","p", None)
        node2 = ParentNode(node1, None, None)
        with self.assertRaises(ValueError):
            ParentNode.to_html(node2)

    def test_no_children(self):
        node1 = ParentNode(None, "p", None)
        with self.assertRaises(ValueError):
            ParentNode.to_html(node1)

    def test_with_props(self):
        node1 = LeafNode(
            "This is sample text", "a", 
            {"href": "https://www.google.com"}
        )
        node2 = ParentNode([node1], "p", None)
        self.assertEqual(
            ParentNode.to_html(node2), 
            "<p><a href='https://www.google.com'>This is sample text</a></p>"
        )
    
    def test_with_children(self):
        node = ParentNode(
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None)
            ], "p"
        )
        self.assertEqual(
            ParentNode.to_html(node), "<p><b>Bold text</b>"
            "Normal text<i>italic text</i>Normal text</p>"

        )

    def test_with_nested_parent(self):
        node1 = ParentNode(
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None)
            ], "p"
        )
        node2 = ParentNode(
            [
                node1,
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None)
            ], "p"
        )
        self.assertEqual(
            ParentNode.to_html(node2), "<p><p><b>Bold text</b>Normal text"
            "<i>italic text</i>Normal text</p>Normal text"
            "<i>italic text</i>Normal text</p>"

        )
    
    def test_with_nested_parents(self):
        node1 = ParentNode(
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None)
            ], "p"
        )
        node2 = ParentNode(
            [
                node1,
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None)
            ], "p"
        )
        node3 = ParentNode(
            [
                LeafNode("Bold text", "b"),
                node2,
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None)
            ], "h1"
        )
        self.assertEqual(
            ParentNode.to_html(node3),
            "<h1><b>Bold text</b><p><p><b>Bold text</b>"
            "Normal text<i>italic text</i>Normal text</p>"
            "Normal text<i>italic text</i>Normal text</p><i>italic text</i>"
            "Normal text</h1>"

        )

class TestLeafNode(unittest.TestCase):
    # Order
    # Value, Tag, Props
    def test_eq(self):
        node = LeafNode("This is sample text", "p", None)
        node2 = LeafNode("This is sample text", "p", None)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = LeafNode("This is sample text", "h1", None)
        node2 = LeafNode("This is sample text", "p", None)
        self.assertNotEqual(node, node2)

    def test_no_props(self):
        node = LeafNode("This is a header.", "h1", None)
        self.assertEqual(LeafNode.to_html(node), "<h1>This is a header.</h1>")

    def test_value_error(self):
        node = LeafNode(None)
        with self.assertRaises(ValueError): 
            LeafNode.to_html(node)

    def test_tag_none(self):
        node = LeafNode("This is sample text", None, None)
        self.assertEqual(LeafNode.to_html(node), "This is sample text")

    def test_props(self):
        node = LeafNode("Click me!", "a", {"href": "https://www.google.com"})
        self.assertEqual(
            LeafNode.to_html(node), 
            "<a href='https://www.google.com'>Click me!</a>"
        )


if __name__ == "__main__":
    unittest.main()