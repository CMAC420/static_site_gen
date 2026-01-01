import os

from src.markdown import markdown_to_html_node
from src.blocks import extract_title


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r")as f:
        template = f.read()
   
    html_node = markdown_to_html_node(markdown)
    content_html = html_node.to_html()
    title = extract_title(markdown)

    page_html = template.replace("{{ Title }}", title)
    page_html = page_html.replace("{{ Content }}", content_html)
    page_html = page_html.replace('href="/', f'href="{basepath}')
    page_html = page_html.replace('src="/', f'src="{basepath}')


    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(page_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for file in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, file)
        dest_path = os.path.join(dest_dir_path, file)
        
        if os.path.isdir(content_path):
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            
            generate_pages_recursive(content_path, template_path, dest_path, basepath)
       
        elif file.endswith(".md"):
            html_name = file.replace(".md", ".html")
            dest_html_path = os.path.join(dest_dir_path, html_name)

            generate_page(content_path, template_path, dest_html_path, basepath)