import unittest

from split_nodes_delimiter import *

class TestSplitNodes(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        self.assertEqual(
            split_nodes_delimiter([node], "`", text_type_code), 
            [TextNode("This is text with a ", "text", None), 
             TextNode("code block", "code", None), TextNode(" word", "text", None)]
        )

    def test_bold(self):
        node = TextNode("This is text with a **bold** word", text_type_text)
        self.assertEqual(
            split_nodes_delimiter([node], "**", text_type_bold), 
            [TextNode("This is text with a ", "text", None), 
             TextNode("bold", "bold", None), TextNode(" word", "text", None)]
        )

    def test_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        self.assertEqual(
            split_nodes_delimiter([node], "*", text_type_italic), 
            [TextNode("This is text with an ", "text", None), 
             TextNode("italic", "italic", None), TextNode(" word", "text", None)]
        ) 

    def test_invalid_text_type(self):
        node = TextNode("This is bold text", text_type_bold)
        self.assertEqual(
            split_nodes_delimiter([node], "**", text_type_bold), 
            [TextNode("This is bold text", "bold", None)]
        ) 

    def test_no_closed_delimiter(self):
        node = TextNode("This is text with a **bold word", text_type_text)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", text_type_bold)


    def test_empty_split_node(self):
        node = TextNode(" *italic* word", text_type_text)
        self.assertEqual(
            split_nodes_delimiter([node], "*", text_type_italic),
            [TextNode(" ", "text", None), TextNode("italic", "italic", None), TextNode(" word", "text", None)]
            )
        
    def test_multiple_nodes(self):
        node = TextNode("This is text with a **bold** word", text_type_text)
        node2 = TextNode("This is text with a **bold** word", text_type_text)
        self.assertEqual(
            split_nodes_delimiter([node, node2], "**", text_type_bold), 
            [TextNode("This is text with a ", "text", None), 
             TextNode("bold", "bold", None), TextNode(" word", "text", None), 
             TextNode("This is text with a ", "text", None), 
             TextNode("bold", "bold", None), TextNode(" word", "text", None)]
        )


if __name__ == "__main__":
    unittest.main()