import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode(
            "This is another text node", "italic", 
            "https://www.facebook.com")
        node2 = TextNode(
            "This is another text node", "italic", 
            "https://www.facebook.com")
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode('print("What a beautiful day for coding")', 
        'code', 'https://www.boot.dev')
        node2 = TextNode('print("What a beautiful day for coding")', 
        'code', 'https://www.boot.dev')
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode('print("What a beautiful day for coding")', 
        'code', 'https://www.boot.dev')
        node2 = TextNode('print("What a beautiful day for coding")', 
        'bold', 'https://www.boot.dev')
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode(
            "This is another text node", "italic")
        node2 = TextNode(
            "This is another text node", "italic", 
            "https://www.facebook.com")
        self.assertNotEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("A test text node this is", "bold")
        self.assertIsNone(node.url)

    def test_is_textnode(self):
        node = TextNode("A test text node this is", "bold")
        self.assertIsInstance(node, TextNode)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_type_text(self):
        node = TextNode("This is sample text.", "text")
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.value, "This is sample text.")
        self.assertIsNone(html_node.tag)
        self.assertIsNone(html_node.props)
    
    def test_text_type_bold(self):
        node = TextNode("This is bold text.", "bold")
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.value, "This is bold text.")
        self.assertEqual(html_node.tag, "b")
        self.assertIsNone(html_node.props)

    def test_text_type_italic(self):
        node = TextNode("This is italic text.", "italic")
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.value, "This is italic text.")
        self.assertEqual(html_node.tag, "i")
        self.assertIsNone(html_node.props)

    def test_text_type_code(self):
        node = TextNode("This is code.", "code")
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.value, "This is code.")
        self.assertEqual(html_node.tag, "code")
        self.assertIsNone(html_node.props)

    def test_text_type_link(self):
        node = TextNode("This is a link.", "link", "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.value, "This is a link.")
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {'href': 'https://www.boot.dev'})

    def test_text_type_image(self):
        node = TextNode("This is an image.", "image", "https://images.google.com")
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(
            html_node.props, 
            {'src': 'https://images.google.com', 'alt': 'This is an image.'}
        )

    def test_invalid_text_type(self):
        node = TextNode("This is sample text.", "invalid")
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(node)
    
        self.assertEqual(str(context.exception), "Invalid TextNode type.")
        
    def test_empty_text(self):
        node = TextNode("", "text")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, "")

    def test_link_empty_url(self):
        node = TextNode("Empty link", "link", "")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.props, {'href': ''})

    def test_case_sensitivity(self):
        node = TextNode("Case Test", "BOLD")
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(node)
        self.assertEqual(str(context.exception), "Invalid TextNode type.")

    def test_special_characters(self):
        node = TextNode("<>&\"'", "text")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, "<>&\"'")




if __name__ == "__main__":
    unittest.main()