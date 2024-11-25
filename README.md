# Markdown2HTML Converter

`markdown2html.py` is a Python script that converts a Markdown file into an HTML file. It supports a variety of Markdown features and some custom syntaxes, making it versatile for your Markdown-to-HTML conversion needs.

## Features

The script supports the following Markdown features and syntaxes:

### Standard Markdown
- **Headers**: Converts `#`, `##`, `###`, ..., up to `######` into `<h1>` to `<h6>` tags.
- **Unordered Lists**: Converts lines starting with `- ` into `<ul>` and `<li>` tags.
- **Ordered Lists**: Converts lines starting with `* ` into `<ol>` and `<li>` tags.
- **Bold Text**: Converts `**text**` into `<b>text</b>`.
- **Italicized Text**: Converts `__text__` into `<em>text</em>`.
- **Paragraphs**: Converts normal text into `<p>` tags.
- **Line Breaks**: Adds `<br />` tags for multiline paragraphs.

### Custom Syntax
- **MD5 Conversion**:
  - Syntax: `[[content]]`
  - Converts the content inside `[[...]]` into its MD5 hash (lowercase).
  - Example: 
    ```markdown
    [[Hello]]
    ```
    Output:
    ```html
    8b1a9953c4611296a827abf8c47804d7
    ```
- **Remove All 'C' Characters**:
  - Syntax: `((content))`
  - Removes all occurrences of the character `c` or `C` from the content inside `((...))`.
  - Example:
    ```markdown
    ((Chicago))
    ```
    Output:
    ```html
    hiago
    ```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/markdown2html.git
   cd markdown2html
   ```

2. Make the script executable:
   ```bash
   chmod +x markdown2html.py
   ```

3. Ensure Python 3 is installed on your system.

## Usage

To convert a Markdown file to an HTML file, run:

```bash
./markdown2html.py <input_file.md> <output_file.html>
```

### Example

Given an `example.md` file:

```markdown
# My title
- Hello
- Bye

((Chicago))

[[Private]]
```

Run the script:

```bash
./markdown2html.py example.md example.html
```

The resulting `example.html` will contain:

```html
<h1>My title</h1>
<ul>
<li>Hello</li>
<li>Bye</li>
</ul>
<p>
hiago
</p>
<p>
2c17c6393771ee3048ae34d6b380c5ec
</p>
```

## Error Handling

- If the input file is missing:
  ```bash
  Missing <input_file.md>
  ```
- If incorrect usage:
  ```bash
  Usage: ./markdown2html.py <input_file.md> <output_file.html>
  ```

## Limitations

- The script assumes strictly valid Markdown and custom syntax.
- Nested custom syntaxes (e.g., `[[((content))]]`) are not supported.
- Undefined behavior for unmatched `[[...]]` or `((...))`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
