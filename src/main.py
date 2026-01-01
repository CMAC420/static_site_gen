import os
import shutil
import sys

from src.utils import copy_static
from src.generate_page import generate_pages_recursive

def main():

    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    copy_static("static", "docs")
    print("Static files copied successfully!")

    generate_pages_recursive(
        "content",
        "template.html",
        "docs",
        basepath
    )

if __name__ == "__main__":
    main()