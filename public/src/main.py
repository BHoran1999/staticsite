from copy_dir import copy_directory
from textnode import TextNode
from generate_pages import generate_pages, generate_pages_recursive 
import sys

def main():

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    else:
        basepath = ""

    print("Using basepath:", basepath)

    copy_directory("static", "docs")

    generate_pages_recursive ("content", "template.html", "docs", basepath)

    print("Site generated successfully")

main()