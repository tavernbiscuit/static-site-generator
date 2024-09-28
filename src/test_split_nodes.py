import unittest

from textnode import (TextNode, text_type_text, text_type_bold, text_type_code, 
text_type_italic, text_type_image, text_type_link)

from split_nodes import (
    split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes)

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

class TestTextToTextNodes(unittest.TestCase):
    def test_simple_text(self):
        text = "Hello, world!"
        self.assertEqual(
            text_to_textnodes(text),
            [TextNode("Hello, world!", text_type_text)]        
        )

    def test_bold_text(self):
        text = "Hello **world**!"
        self.assertEqual(
            text_to_textnodes(text),
            [TextNode("Hello ", text_type_text),
            TextNode("world", text_type_bold),
            TextNode("!", text_type_text),]       
        )

    def test_italic_text(self):
        text = "Hello *world*!"
        self.assertEqual(
            text_to_textnodes(text),
            [TextNode("Hello ", text_type_text),
            TextNode("world", text_type_italic),
            TextNode("!", text_type_text),]       
        )

    def test_code_text(self):
        text = "Hello `world`!"
        self.assertEqual(
            text_to_textnodes(text),
            [TextNode("Hello ", text_type_text),
            TextNode("world", text_type_code),
            TextNode("!", text_type_text),]       
        )

    def test_link_text(self):
        text = "Check out [this link](https://example.com)"
        self.assertEqual(
            text_to_textnodes(text),
            [TextNode("Check out ", text_type_text),
            TextNode("this link", text_type_link, "https://example.com")]
        )

    def test_image_text(self):
        text = "Here's an image: ![alt text](https://example.com/image.jpg)"
        self.assertEqual(
            text_to_textnodes(text),
            [TextNode("Here's an image: ", text_type_text),
            TextNode("alt text", text_type_image, "https://example.com/image.jpg")]       
        )

    def test_mixed_text(self):
        text = "This is **bold** and *italic* and `code`"
        self.assertEqual(
            text_to_textnodes(text),
            [TextNode("This is ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" and ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" and ", text_type_text),
            TextNode("code", text_type_code)]       
        )

if __name__ == "__main__":
    unittest.main()