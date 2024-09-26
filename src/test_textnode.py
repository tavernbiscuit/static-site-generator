import unittest

from textnode import TextNode


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
    

if __name__ == "__main__":
    unittest.main()