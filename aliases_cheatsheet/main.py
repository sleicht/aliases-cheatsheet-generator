import os

from aliases_cheatsheet.alias_loader import load_git_aliases, load_shell_aliases
from aliases_cheatsheet.content_generator import (
    generate_html_content,
    generate_html_table,
    generate_markdown,
)
from aliases_cheatsheet.file_writer import (
    write_to_html_file,
    write_to_markdown_file,
    write_to_pdf_file,
)


aliases_file = os.path.expanduser("~/.aliases")
gitconfig_file = os.path.expanduser("~/.gitconfig")


def main():
    # Load aliases and explanations
    shell_aliases, shell_explanations = load_shell_aliases(aliases_file)
    git_aliases, git_explanations = load_git_aliases(gitconfig_file)

    # Generate content
    document = "# Personal (auto-generated) Aliases Cheatsheet\n\n"
    document += "## Find aliases with ease\n\n"
    document += "Make your Shell and Git aliases easy to view and search\n\n"
    document += generate_markdown(shell_aliases, "Shell", shell_explanations)
    document += "\n"
    document += generate_markdown(git_aliases, "Git", git_explanations)

    # Prepare HTML content
    shell_table_rows = generate_html_table(shell_aliases, shell_explanations)
    git_table_rows = generate_html_table(git_aliases, git_explanations)
    html_content = generate_html_content(shell_table_rows, git_table_rows)

    # Write to files
    write_to_markdown_file(document, "aliases.md")
    write_to_html_file(html_content, "aliases.html")
    write_to_pdf_file(document, "aliases.pdf")


if __name__ == "__main__":
    main()
