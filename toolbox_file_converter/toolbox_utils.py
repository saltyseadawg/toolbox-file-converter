import re


def get_toolbox_tag(toolbox_line: str) -> str:
    """Gets the toolbox tag."""

    tag_regex = re.compile(r"\\(\S*)")
    result = re.search(tag_regex, rf"{toolbox_line}")
    return result.group(1) if result else None


def remove_tag(toolbox_line: str, tag: str) -> str:
    """Removes beginning tag from toolbox_line."""
    new_line = toolbox_line.replace(rf"\{tag} ", "", 1)
    return rf"{new_line}"
