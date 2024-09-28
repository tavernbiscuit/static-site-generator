import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type

class TestMarkdownBlocks(unittest.TestCase):
    def test_eq(self):
        text = ("# This is a heading"
            "\n\n"
            "This is a paragraph of text. It has some **bold** "
            "and *italic* words inside of it."
            "\n\n"
            "* This is the first list item in a list block"
            "* This is a list item"
            "* This is another list item")
        self.assertEqual(
            markdown_to_blocks(text),
            ['# This is a heading', 
             'This is a paragraph of text. It has some **bold** '
             'and *italic* words inside of it.', 
             '* This is the first list item in a list block* '
             'This is a list item* This is another list item']
        )

    def test_eq2(self):
        text = ("# This is a heading"
            "\n\n"
            "This is a paragraph of text. It has some **bold** "
            "and *italic* words inside of it."
            "\n\n"
            "* This is the first list item in a list block"
            "\n\n"
            "* This is a list item\n"
            "* This is another list item")
        self.assertEqual(
            markdown_to_blocks(text),
            ['# This is a heading', 
             'This is a paragraph of text. It has some **bold** '
             'and *italic* words inside of it.', 
             '* This is the first list item in a list block',
             '* This is a list item\n* This is another list item']
        )

    def test_empty_input(self):
        text = ("")
        self.assertEqual(
            markdown_to_blocks(text),
            []
        )

    def test_only_whitespace(self):
        text = ("    ""\n\n""     ""     ""\n\n""    ")
        self.assertEqual(
            markdown_to_blocks(text),
            []
        )

    def test_excessive_newlines(self):
        text = "Block 1\n\n\n\nBlock 2\n\n\n\n\nBlock 3"
        self.assertEqual(
            markdown_to_blocks(text),
            ['Block 1', 'Block 2', 'Block 3']
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "Paragraph text"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_heading(self):
        block = "# Heading"
        self.assertEqual(block_to_block_type(block), "heading")

    def test_heading2(self):
        block = "###### Heading 6"
        self.assertEqual(block_to_block_type(block), "heading")

    def test_code(self):
        block = "```This is code text!```"
        self.assertEqual(block_to_block_type(block), "code")
    
    def test_unordered_list(self):
        block = "* item number 1\n- item number 2\n- another item\n* one more item"
        self.assertEqual(block_to_block_type(block), "unordered_list")

    def test_ordered_list(self):
        block = "1. item number one\n2. item number two\n3. item number three"
        self.assertEqual(block_to_block_type(block), "ordered_list")

    def test_ordered_list2(self):
        block = "1. item number one\n2. item number two\n4. item number three"
        self.assertNotEqual(block_to_block_type(block), "ordered_list")
            

if __name__ == "__main__":
    unittest.main() 