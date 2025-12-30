import unittest

from src.textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("hello", TextType.TEXT)
        node2 = TextNode("goodbye", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_type_not_equal(self):
        node = TextNode("hello", TextType.TEXT)
        node2 = TextNode("hello", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


    

if __name__ == "__main__":
    unittest.main()