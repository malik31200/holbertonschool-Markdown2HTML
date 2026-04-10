#!/usr/bin/python3
"""
Module that converts a Markdown file to HTML.
Handles headings and unordered lists.
"""

import sys
import os


def convert_heading(line):
    """Convert markdown heading to HTML"""
    if line.startswith("#"):
        count = 0
        while count < len(line) and line[count] == "#":
            count += 1

        if count <= 6 and count < len(line) and line[count] == " ":
            content = line[count + 1:].strip()
            return f"<h{count}>{content}</h{count}>"
    return None


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

    in_list = False

    with open(output_file, "w", encoding="utf-8") as html_file:
        for line in lines:
            line = line.rstrip()

            # Gestion des headings
            heading = convert_heading(line)
            if heading:
                if in_list:
                    html_file.write("</ul>\n")
                    in_list = False
                html_file.write(heading + "\n")
                continue

            # Gestion des listes "- "
            if line.startswith("- "):
                if not in_list:
                    html_file.write("<ul>\n")
                    in_list = True
                content = line[2:].strip()
                html_file.write(f"<li>{content}</li>\n")
                continue

            # Si on sort d'une liste
            if in_list:
                html_file.write("</ul>\n")
                in_list = False

            # Ligne normale (optionnel pour maintenant)
            if line:
                html_file.write(line + "\n")

        # Fermer la liste si fichier finit dedans
        if in_list:
            html_file.write("</ul>\n")

    sys.exit(0)


if __name__ == "__main__":
    main()
