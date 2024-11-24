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
            in_list = False  # Track whether we are inside a list
            for line in input_file:
                line = line.strip()

                # End the list if necessary
                if in_list and not line.startswith('- '):
                    output_file.write("</ul>\n")  # Close the list
                    in_list = False

                # Check for headings
                if line.startswith("#"):
                    heading_level = len(line.split(" ")[0])
                    if 1 <= heading_level <= 6:
                        content = line[heading_level:].strip()
                        output_file.write(f"<h{heading_level}>{content}</h{heading_level}>\n")

                # Check for list items
                elif line.startswith('- '):
                    if not in_list:
                        output_file.write("<ul>\n")  # Start a new unordered list
                        in_list = True
                    content = line[2:].strip()  # Remove "- " prefix
                    output_file.write(f"<li>{content}</li>\n")

            # If the file ends while inside a list, close the list
            if in_list:
                output_file.write("</ul>\n")

        # Exit successfully
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)
