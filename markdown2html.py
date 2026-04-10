#!/usr/bin/python3


"""
Module that converts a Markdown file to HTML.
"""

import sys
import os


def main():
    """Main function"""
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Lire le fichier Markdown
    with open(input_file, "r", encoding="utf-8") as md_file:
        content = md_file.read()

    # Pour cette tâche : copie simple (pas encore de conversion)
    with open(output_file, "w", encoding="utf-8") as html_file:
        html_file.write(content)

    sys.exit(0)


if __name__ == "__main__":
    main()
