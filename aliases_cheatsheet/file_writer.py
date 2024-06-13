import markdown
import pdfkit


def write_to_markdown_file(content, file_path):
    with open(file_path, "w") as file:
        file.write(content)
    print(f"Markdown document generated: {file_path}")


def write_to_html_file(content, file_path):
    with open(file_path, "w") as file:
        file.write(content)
    print(f"HTML document generated: {file_path}")


def write_to_pdf_file(html_content, pdf_path):
    pdfkit.from_string(html_content, pdf_path)
    print(f"PDF document generated: {pdf_path}")
