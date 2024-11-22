#!/usr/bin/python3
"""This module converts a Markdown file to an HTML file."""
import sys
import os


if __name__ == "__main__":
    # Check if the number of arguments is less than 3
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.exists(input_filename):
        sys.stderr.write(f"Missing {input_filename}\n")
        sys.exit(1)

    try:
        with open(input_filename, "r") as input_file, open(output_filename, "w") as output_file:
            in_unordered_list = False  # Track whether we are inside an unordered list
            in_ordered_list = False
            in_paragraph = False  # Track whether we are inside a paragraph
            for line in input_file:
                line = line.strip()

                if len(line) != 0:
                    character = line[0] # Get the first character

                # End the unordered list if necessary
                if in_unordered_list and not line.startswith('- '):
                    output_file.write("</ul>\n")  # Close the list
                    in_unordered_list = False

                # End the ordered list if necessary
                if in_ordered_list and not line.startswith('* '):
                    output_file.write("</ol>\n")
                    in_ordered_list = False

                # End paragraph if necessary
                if in_paragraph and not line:
                    output_file.write("</p>\n")
                    in_paragraph = False

                # Check for headings
                if line.startswith("#"):
                    heading_level = len(line.split(" ")[0])
                    if 1 <= heading_level <= 6:
                        content = line[heading_level:].strip()
                        output_file.write(f"<h{heading_level}>{content}</h{heading_level}>\n")

                # Check for unordered list items
                elif line.startswith('- '):
                    if not in_unordered_list:
                        output_file.write("<ul>\n")  # Start a new unordered list
                        in_unordered_list = True
                    content = line[2:].strip()  # Remove "- " prefix
                    output_file.write(f"<li>{content}</li>\n")

                # Check for unordered list items
                elif line.startswith('* '):
                    if not in_ordered_list:
                        output_file.write("<ol>\n")
                        in_ordered_list = True
                    content = line[2:].strip()
                    output_file.write(f"<li>{content}</li>\n")

                # Handle paragraphs
                elif line:
                    if not in_paragraph:
                        output_file.write("<p>\n")
                        in_paragraph = True
                    else:
                        output_file.write("<br />\n")
                    output_file.write(line + "\n")

            # Close any remaining open tags
            if in_unordered_list:
                output_file.write("</ul>\n")
            if in_ordered_list:
                output_file.write("</ol>\n")
            if in_paragraph:
                output_file.write("</p>\n")

        # Exit successfully
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)
