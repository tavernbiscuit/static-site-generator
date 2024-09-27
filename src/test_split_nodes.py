import unittest

from split_nodes import *

class TestSplitNodesDelimiter(unittest.TestCase):
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

class TestSplitNodesLink(unittest.TestCase):
    def test_link_eq(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev)"
            " and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        self.assertEqual(
            split_nodes_link([node]),
                     [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode(
                "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
            ),
        ]      
        )

    def test_broken_link(self):
        node = TextNode(
            "This is text with a link to boot dev](https://www.boot.dev)"
            " and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        self.assertEqual(
            split_nodes_link([node]),
                     [
            TextNode("This is text with a link to boot dev]"
                     "(https://www.boot.dev) and ", text_type_text),
            TextNode(
                "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
            ),
        ]      
        )

    def test_broken_link2(self):
        node = TextNode(
            "This is text with a link to boot dev](https://www.boot.dev)"
            " and [to youtube(https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        self.assertEqual(
            split_nodes_link([node]),
                     [
            TextNode("This is text with a link to boot dev]"
                     "(https://www.boot.dev) and"
                     " [to youtube(https://www.youtube.com/@bootdotdev)", text_type_text),
        ]      
        )

    def test_empty_link(self):
        node = TextNode(
            "This is text with a link [](https://www.boot.dev)"
            " and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        self.assertEqual(
            split_nodes_link([node]),
                     [
            TextNode("This is text with a link ", text_type_text),
            TextNode("", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode(
                "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
            ),
        ]      
        )

class TestSplitNodesImage(unittest.TestCase):
    def test_image_eq(self):
        node = TextNode(
            "This is text with an image ![to boot dev](https://www.boot.dev)"
            " and ![to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        self.assertEqual(
            split_nodes_image([node]),
                     [
            TextNode("This is text with an image ", text_type_text),
            TextNode("to boot dev", text_type_image, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode(
                "to youtube", text_type_image, "https://www.youtube.com/@bootdotdev"
            ),
        ]      
        )

    def test_broken_image(self):
        node = TextNode(
            "This is text with an image at boot dev](https://www.boot.dev)"
            " and ![to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        self.assertEqual(
            split_nodes_image([node]),
                     [
            TextNode("This is text with an image at boot dev]"
                     "(https://www.boot.dev) and ", text_type_text),
            TextNode(
                "to youtube", text_type_image, "https://www.youtube.com/@bootdotdev"
            ),
        ]      
        )

    def test_broken_image2(self):
        node = TextNode(
            "This is text with an image at boot dev](https://www.boot.dev)"
            " and [at youtube(https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        self.assertEqual(
            split_nodes_image([node]),
                     [
            TextNode("This is text with an image at boot dev]"
                     "(https://www.boot.dev) and"
                     " [at youtube(https://www.youtube.com/@bootdotdev)", text_type_text),
        ]      
        )

    def test_empty_alt_text(self):
        node = TextNode(
            "This is text with an image at link ![](https://www.boot.dev)"
            " and ![at youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        self.assertEqual(
            split_nodes_image([node]),
                     [
            TextNode("This is text with an image at link ", text_type_text),
            TextNode("", text_type_image, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode(
                "at youtube", text_type_image, "https://www.youtube.com/@bootdotdev"
            ),
        ]      
        )

if __name__ == "__main__":
    unittest.main()