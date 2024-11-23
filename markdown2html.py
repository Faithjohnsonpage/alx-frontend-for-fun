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

    # If all checks pass, exit successfully
    sys.exit(0)
