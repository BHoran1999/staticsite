from copy_dir import copy_directory
from textnode import TextNode
from generate_pages import generate_pages, generate_pages_recursive 
import sys

def main():

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    else:
        basepath = "/"

    copy_directory("static", "docs")

    generate_pages("content/index.md", "template.html", "docs/index.html", basepath)

    generate_pages_recursive ("content", "template.html", "docs", basepath)

main()