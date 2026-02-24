import os
from extract_title import extract_title
import re
from markdown_to_html_node import markdown_to_html_node

def generate_pages(from_path, template_path, to_path, basepath):
    print(f"Generating page from {from_path} to {to_path} using template {template_path}")
    
    with open(from_path, 'r', encoding='utf-8') as f:
        markdown = f.read()

    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    node = markdown_to_html_node(markdown)
    title = extract_title(markdown)
    html_content = node.to_html()


    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", html_content)
    html = html.replace('{{href="/}}', f'{{href="{basepath}"}}' )
    html = html.replace('{{src="/}}', f'{{src="{basepath}"}}' )


    os.makedirs(os.path.dirname(to_path), exist_ok=True)

    with open(to_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print("Page generated successfully")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):

    for item in os.listdir(dir_path_content):

        content_path = os.path.join(dir_path_content, item)

        if os.path.isdir(content_path):
            dest_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(content_path, template_path, dest_path, basepath)
        elif item.endswith(".md"):
            html_file_name = item[:-3] + ".html"
            dest_path = os.path.join(dest_dir_path, html_file_name)
            generate_pages(content_path, template_path, dest_path, basepath)
        else:
            dest_path = os.path.join(dest_dir_path, item)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            with open(content_path, 'r', encoding='utf-8') as f:
                content = f.read()
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(content)

    