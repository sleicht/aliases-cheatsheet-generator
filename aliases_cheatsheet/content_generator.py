def abbreviate_command(command, max_length=30):
    if len(command) > max_length:
        return command[:max_length] + "..."
    return command


def generate_markdown(aliases, alias_type, explanations):
    markdown_text = f"## {alias_type.capitalize()} Aliases\n\n"
    for alias, command in aliases.items():
        description = explanations.get(alias, "")
        abbrev_command = abbreviate_command(command)
        markdown_text += f"- **{alias}**: `{abbrev_command}`"
        if description:
            markdown_text += f" - _{description}_"
        markdown_text += "\n"
    return markdown_text


def generate_html_table(aliases, explanations):
    table_rows = ""
    for alias, command in aliases.items():
        comment = explanations.get(alias, "")
        abbrev_command = abbreviate_command(command)
        table_rows += (
            f"<tr><td>{alias}</td><td>{abbrev_command}</td><td>{comment}</td></tr>"
        )
    return table_rows


def generate_html_content(shell_table_rows, git_table_rows):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Personal (auto-generated) Aliases Cheatsheet</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                color: #333;
                background-color: #f9faff;
            }}
            h1 {{
                text-align: center;
                color: #ff6f61;
                margin-bottom: 5px;
            }}
            h2 {{
                text-align: center;
                color: #ff9671;
                margin-bottom: 5px;
            }}
            p {{
                text-align: center;
                color: #ffc75f;
            }}
            .search-box {{
                text-align: center;
                margin: 20px 0;
            }}
            input[type="text"] {{
                width: 50%;
                padding: 10px;
                font-size: 16px;
                margin-top: 10px;
                border: 1px solid #ccc;
                border-radius: 4px;
                background-color: #d4f1f4;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
                border: 2px solid #ff6f61;
            }}
            th, td {{
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #ff9671;
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #ffeebb;
            }}
            tr:hover {{
                background-color: #d4f1f4;
            }}
        </style>
        <script>
            function searchAliases() {{
                var input, filter, table, tr, td, i, j, txtValue;
                input = document.getElementById('searchInput');
                filter = input.value.toUpperCase();
                tables = [document.getElementById("shellAliasTable"), document.getElementById("gitAliasTable")];
                for (ti = 0; ti < tables.length; ti++) {{
                    table = tables[ti];
                    tr = table.getElementsByTagName('tr');
                    for (i = 1; i < tr.length; i++) {{
                        tr[i].style.display = "none";
                        td = tr[i].getElementsByTagName("td");
                        for (j = 0; j < td.length; j++) {{
                            if (td[j]) {{
                                txtValue = td[j].textContent || td[j].innerText;
                                if (txtValue.toUpperCase().indexOf(filter) > -1) {{
                                    tr[i].style.display = "";
                                    break;
                                }}
                            }}
                        }}
                    }}
                }}
            }}
        </script>
    </head>
    <body>
        <h1>Personal (auto-generated) Aliases Cheatsheet</h1>
        <h2>Find aliases with ease</h2>
        <p>Make your Shell and Git aliases easy to view and search</p>
        <div class="search-box">
            <input type="text" id="searchInput" onkeyup="searchAliases()" placeholder="Search for aliases..">
        </div>
        <h2>Shell Aliases</h2>
        <table id="shellAliasTable">
            <tr>
                <th>Alias</th>
                <th>Definition</th>
                <th>Comment</th>
            </tr>
            {shell_table_rows}
        </table>
        <h2>Git Aliases</h2>
        <table id="gitAliasTable">
            <tr>
                <th>Alias</th>
                <th>Definition</th>
                <th>Comment</th>
            </tr>
            {git_table_rows}
        </table>
    </body>
    </html>
    """
    return html_content
