import re
import xml.etree.ElementTree as ET



def get_toolbox_tag(toolbox_line: str) -> str:
    """Gets the toolbox tag."""

    tag_regex = re.compile('\\\\(.*) ')
    result = re.search(tag_regex, toolbox_line)
    return result.group(1) if result else None

    