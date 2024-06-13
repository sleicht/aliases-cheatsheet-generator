import configparser
import os


def load_shell_aliases(file_path):
    aliases = {}
    explanations = {}
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            comment = ""
            for line in f:
                line = line.strip()
                if line.startswith("alias"):
                    alias = line.split("alias ")[1]
                    name, command = alias.split("=", 1)
                    name = name.strip()
                    command = command.strip().strip("'").strip('"')
                    aliases[name] = command
                    if comment:
                        explanations[name] = comment
                        comment = ""
                elif line.startswith("##"):
                    comment = line.lstrip("## ").strip()
    return aliases, explanations


def load_git_aliases(file_path):
    aliases = {}
    explanations = {}
    if os.path.exists(file_path):
        config = configparser.ConfigParser()
        with open(file_path, "r") as f:
            config.read_file(f)
        with open(file_path, "r") as f:
            in_alias_section = False
            comment = ""
            for line in f:
                line = line.strip()
                if line.startswith("[alias]"):
                    in_alias_section = True
                    comment = ""
                elif line.startswith("[") and in_alias_section:
                    in_alias_section = False
                elif in_alias_section:
                    if line.startswith(";"):
                        comment = line.lstrip("; ").strip()
                    elif "=" in line and not line.startswith(";"):
                        name, command = line.split("=", 1)
                        name = name.strip()
                        aliases[name] = command.strip()
                        if comment:
                            explanations[name] = comment
                            comment = ""
    return aliases, explanations
