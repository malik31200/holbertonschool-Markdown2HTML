#!/usr/bin/python3
"""
Module that converts a Markdown file to HTML.
Handles headings from # to ######
"""

import sys
import os


def convert_line(line):
    """Convert a single markdown line to HTML"""
    line = line.rstrip()

    # Gestion des headings (# à ######)
    if line.startswith("#"):
        count = 0
        while count < len(line) and line[count] == "#":
            count += 1

        # Vérifie qu'il y a un espace après les #
        if count <= 6 and count < len(line) and line[count] == " ":
            content = line[count + 1:]
            return f"<h{count}>{content}</h{count}>"

    return line


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

    with open(input_file, "r", encoding="utf-8") as md_file:
        lines = md_file.readlines()

    with open(output_file, "w", encoding="utf-8") as html_file:
        for line in lines:
            html_line = convert_line(line)
            html_file.write(html_line + "\n")

    sys.exit(0)


if __name__ == "__main__":
    main()
