# import click
from lxml import etree as ET

from toolbox_file_converter import toolbox_utils


# @click.command()
# @click.option("-f", "--toolboxfile", required=True)
# @click.option("-o", "--output", required=True)
# @click.option("-t", "--tag", required=True)
# @click.option("-l", "--lang", required=True)
def convert(filename, output, tag, lang):
    """
    Converts in_file into an xml out_file for Readalongs Studio.
    Exclude_tags are converted into xml objects that won't be aligned.
    """
    NSMAP = {"lang": lang}

    div_attr = {"type": "page"}

    no_align_attr = {"do-not-align": "true"}

    root = ET.Element("TEI")
    tree = ET.ElementTree(root)
    text = ET.SubElement(root, "text", nsmap=NSMAP)
    body = ET.SubElement(text, "body")

    # Assuming that only one tag will be aligned
    with open(filename) as fp:
        lines = fp.readlines()
        page = ET.SubElement(body, "div", div_attr)
        p_element = ET.SubElement(page, "p")
        for line in lines:
            if not line.strip():
                continue
            line_tag = toolbox_utils.get_toolbox_tag(line)
            if line_tag == tag:
                page = ET.SubElement(body, "div", div_attr)
                p_element = ET.SubElement(page, "p")
                ET.SubElement(p_element, "s").text = toolbox_utils.remove_tag(
                    line, line_tag
                )
            else:
                ET.SubElement(
                    p_element, "s", no_align_attr
                ).text = toolbox_utils.remove_tag(line, line_tag)

    tree.write(output, xml_declaration=True, encoding="UTF-8", pretty_print=True)
