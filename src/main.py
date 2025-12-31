import os
from src.utils import copy_static
from src.generate_page import generate_page

def main():
    if os.path.exists("public"):
        import shutil
        shutil.rmtree("public")
    
    copy_static("static", "public")
    print("Static files copied successfully!")

    generate_page(
        "content/index.md",
        "template.html",
        "public/index.html"
    )

if __name__ == "__main__":
    main()