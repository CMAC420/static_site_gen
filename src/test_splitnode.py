import unittest

from src.textnode import TextNode, TextType
from src.splitnode import split_node_delimiter, split_node_image, split_node_link

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

class TestSplitNodesImage(unittest.TestCase):
    def test_single_image(self):
        node = TextNode("Here is an image ![alt](https://img.com.au/a.png) end", TextType.TEXT)
        result = split_node_image([node])
        self.assertEqual(result, [
            TextNode("Here is an image ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "https://img.com.au/a.png"),
            TextNode(" end", TextType.TEXT),
        ])

    def test_multiple_images(self):
        node = TextNode("![a](url1) middle ![b](url2)", TextType.TEXT)
        result = split_node_image([node])
        self.assertEqual(result,[
            TextNode("a", TextType.IMAGE, "url1"),
            TextNode(" middle ", TextType.TEXT),
            TextNode("b", TextType.IMAGE, "url2"),
        ])

    def test_no_image(self):
        node = TextNode("no image here", TextType.TEXT)
        self.assertEqual(split_node_image([node]), [node])

class TestSplitNodeLinks(unittest.TestCase):
    def test_single_link(self):
        node = TextNode("Click [here](https://example.com) now", TextType.TEXT)
        result = split_node_link([node])
        self.assertEqual(result, [
            TextNode("Click ", TextType.TEXT),
            TextNode("here", TextType.LINK, "https://example.com"),
            TextNode(" now", TextType.TEXT),
        ])
        
    def test_multiple_links(self):
        node = TextNode("[one](url1) middle [two](url2)", TextType.TEXT)
        result = split_node_link([node])
        self.assertEqual(result, [
            TextNode("one", TextType.LINK, "url1"),
            TextNode(" middle ", TextType.TEXT),
            TextNode("two", TextType.LINK, "url2"),
        ])

    def test_no_links(self):
        node = TextNode("there is no link", TextType.TEXT)
        self.assertEqual(split_node_link([node]),[node])

if __name__ == "__main__":
    unittest.main()