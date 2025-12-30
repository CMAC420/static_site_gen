import unittest

from src.textnode import TextNode, TextType
from src.text import text_to_text_node



class TestTextNode(unittest.TestCase):
    def test_full_example(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
            "and a [link](https://boot.dev)"
        )
        
        node = text_to_text_node(text)

        self.assertEqual(node, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

    def test_text_only(self):
        text = "This is just plain text"
        node = text_to_text_node(text)
        self.assertEqual(node, [TextNode(text, TextType.TEXT)])

    def test_bold_only(self):
        text = "**This is bold text**"
        node = text_to_text_node(text)
        self.assertEqual(node, [TextNode("This is bold text", TextType.BOLD)])

if __name__ == "__main__":
    unittest.main()