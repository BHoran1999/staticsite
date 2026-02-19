from copy_dir import copy_directory
from textnode import TextNode
from generate_pages import generate_pages, generate_pages_recursive 

def main():

    #copy_directory("static", "public")

    #generate_pages("content/index.md", "template.html", "public/index.html")

    generate_pages_recursive ("content", "template.html", "public")

main()