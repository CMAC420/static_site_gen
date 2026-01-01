# STATIC SITE GENERATOR (PYTHON)

A simple static_site_generator written in Python that converts Markdown files into HTML pages.
It supports headings, paragraphs, lists, quotes, code blocks, inline formatting, images and links.
It can be deployed to GitHub Pages.

# FEATURES
- Converts Markdown to HTML
- Supports block types:
    - Headings
    - Paragraphs
    - Code blocks
    - Blockquotes
    - Ordered and Unordered lists
- Supports inline Markdown:
    - **Bold**
    - _Italic_
    - `Code`
    - Links and images
- Recursivley igenerates pages from nested content directories
- Copies static assets (CSS, images)
- Configures base path for GitHub Pages deployment

TO RUN LOCALLY:
bash

./main.sh

THEN OPEN YOUR BROWERS AT:

http://localhost:8888

TO RUN IN GITHUB PAGES:

./build.sh

This generates the site into the docs/ directory using a base path that matches the repository name.


TESTING
- Markdown parsing
- Block type detection
- Inline formatting
- Node conversions

Tests can be run with:
bash

python3 -m unittest


This project was built for educational purposes as a part of the Boot.dev curriculum.