#!/usr/bin/python3
"""This module converts a Markdown file to an HTML file."""
import sys
import os
import re

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    if not os.path.exists(input_filename):
        sys.stderr.write(f"Missing {input_filename}\n")
        sys.exit(1)

    try:
        with open(input_filename, "r") as input_file, open(output_filename, "w") as output_file:
            in_unordered_list = False
            in_ordered_list = False
            in_paragraph = False

            for line in input_file:
                line = line.strip()

                if not line and in_paragraph:
                    output_file.write("</p>\n")
                    in_paragraph = False

                if line.startswith("#"):
                    heading_level = len(line.split(" ")[0])
                    if 1 <= heading_level <= 6:
                        content = line[heading_level:].strip()
                        output_file.write(f"<h{heading_level}>{content}</h{heading_level}>\n")

                elif line.startswith('- '):
                    if not in_unordered_list:
                        output_file.write("<ul>\n")
                        in_unordered_list = True
                    content = line[2:].strip()
                    content = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', content)
                    content = re.sub(r'__(.+?)__', r'<em>\1</em>', content)
                    output_file.write(f"<li>{content}</li>\n")

                elif line.startswith('* '):
                    if not in_ordered_list:
                        output_file.write("<ol>\n")
                        in_ordered_list = True
                    content = line[2:].strip()
                    content = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', content)
                    content = re.sub(r'__(.+?)__', r'<em>\1</em>', content)
                    output_file.write(f"<li>{content}</li>\n")

                else:
                    if not in_paragraph:
                        output_file.write("<p>\n")
                        in_paragraph = True
                    else:
                        output_file.write("<br />\n")
                    line = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)
                    line = re.sub(r'__(.+?)__', r'<em>\1</em>', line)
                    output_file.write(line + "\n")

            if in_unordered_list:
                output_file.write("</ul>\n")
            if in_ordered_list:
                output_file.write("</ol>\n")
            if in_paragraph:
                output_file.write("</p>\n")

        sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)
