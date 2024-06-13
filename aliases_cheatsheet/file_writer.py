import markdown2
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def write_to_markdown_file(content, file_path):
    with open(file_path, "w") as file:
        file.write(content)
    print(f"Markdown document generated: {file_path}")


def write_to_html_file(content, file_path):
    with open(file_path, "w") as file:
        file.write(content)
    print(f"HTML document generated: {file_path}")


def strip_custom_lines(html_content):
    lines_to_remove = [
        # HTML converted lines that should be skipped
        "<h1>Personal (auto-generated) Aliases Cheatsheet</h1>",
        "<h2>Find aliases with ease</h2>",
        "<p>Make your Shell and Git aliases easy to view and search</p>",
    ]
    for line in lines_to_remove:
        html_content = html_content.replace(line, "").replace(
            "\n\n", "\n"
        )  # Remove and correct double newlines
    return html_content


def write_to_pdf_file(md_content, pdf_path):
    html_content = markdown2.markdown(md_content)
    html_content = strip_custom_lines(html_content)
    document = SimpleDocTemplate(pdf_path, pagesize=letter)

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        name="Title",
        fontSize=18,
        leading=22,
        alignment=1,
        spaceAfter=20,
        textColor="#333",
    )
    subtitle_style = ParagraphStyle(
        name="Subtitle",
        fontSize=14,
        leading=18,
        alignment=1,
        spaceAfter=10,
        textColor="#666",
    )
    body_style = styles["Normal"]
    body_style.fontSize = 10

    story = []

    # Add custom title and subtitle only once
    story.append(Paragraph("Personal (auto-generated) Aliases Cheatsheet", title_style))
    story.append(Paragraph("Find aliases with ease", subtitle_style))
    story.append(
        Paragraph("Make your Shell and Git aliases easy to view and search", body_style)
    )
    story.append(Spacer(1, 0.2 * inch))

    for line in html_content.split("\n"):
        if line.strip():
            # Adjust headers and paragraphs differently
            if line.startswith("<h1>"):
                # Skip the custom title
                pass
            elif line.startswith("<h2>"):
                # Skip the custom subtitle
                pass
            else:
                story.append(Paragraph(line, body_style))
                story.append(Spacer(1, 0.2 * inch))

    document.build(story)
    print(f"PDF document generated: {pdf_path}")
