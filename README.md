# Aliases Cheatsheet

> Personal (auto-generated) Aliases Cheatsheet for Shell and Git aliases. This project provides an easy way to manage and view your aliases in Markdown, HTML, and PDF formats.

[![GitHub tag](https://img.shields.io/github/tag/sleicht/aliases-cheatsheet-generator?include_prereleases=&sort=semver&color=blue)](https://github.com/sleicht/aliases-cheatsheet-generator/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

## Features

-   Extract aliases and their descriptions from `.aliases` and `.gitconfig` files.
-   Generate a Markdown document with all aliases.
-   Generate a styled HTML document with a search filter to find aliases quickly.
-   Generate a PDF document from the HTML content.

## Installation

### Prerequisites

-   **Python 3** should be installed on your machine.
-   **wkhtmltopdf** for PDF generation:

- **macOS**: `brew install wkhtmltopdf`
- **Linux**: `sudo apt-get install wkhtmltopdf`
- **Windows**: Download and install from the [official website](https://wkhtmltopdf.org/downloads.html).

### Steps

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/aliases-cheatsheet.git
    cd aliases-cheatsheet
    ```

2. **Create a virtual environment**:

    ```sh
    make venv
    ```

3. **Install the dependencies**:

    ```sh
    make install_deps
    ```

4. **Generate the files**:

    ```sh
    make generate_files
    ```

## Usage

-   **Markdown Document**: `aliases.md`
-   **HTML Document**: `aliases.html`
-   **PDF Document**: `aliases.pdf`

## Comment Formatting

To ensure comments are correctly read and included in the generated files, follow the below-specific formatting rules:

### Shell Aliases (`.aliases`)
Use comments prefixed with `##` directly above each alias definition.

Example `.aliases` file:

```bash
## Lists files in long format
alias ll='ls -la'
## Shows the status of the git repo
alias gs='git status'
## Pushes commits to the remote repo
alias gp='git push'
```

### Git Aliases (`.aliases`)

Use comments prefixed with a semicolon `;` directly above each alias definition within the `[alias]` section.

Example `.gitconfig` file:

```
[alias]
    ; Checkout branches
    co = checkout
    ; List branches
    br = branch
    ; Commit changes
    ci = commit
```

## Sample

You can turn those into a searchable webpage that looks like this:

<div align="center">

![Sample screenshot](/sample.png)

</div>

## License

Released under [MIT](/LICENSE) by [@sleicht](https://github.com/sleicht).
