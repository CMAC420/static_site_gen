import unittest

from src.textnode import *
from src.splitnode import split_node_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_split(self):
        node = TextNode("Hello `world`", TextType.TEXT)
        result = split_node_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "Hello ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "world")
        self.assertEqual(result[1].text_type, TextType.CODE)

    def test_bold_split(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_node_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        

    def test_unmatched_delimiter(self):
        node = TextNode("This is **broken", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_node_delimiter([node], "**", TextType.BOLD)

if __name__ == "__main__":
    unittest.main()