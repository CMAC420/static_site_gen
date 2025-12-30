import unittest

from src.extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtracedMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_url(self):
        matches = extract_markdown_links(
            "This is a text with a link [to boot dev](https://www.boot.dev) "
            "and [to youtube](https://www.youtube.com/@boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"),("to youtube", "https://www.youtube.com/@boot.dev")], matches)

    def test_images_not_links(self):
        text = "![image](https://example.com)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()