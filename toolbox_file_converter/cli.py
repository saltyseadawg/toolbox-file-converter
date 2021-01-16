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

    # attr_qname = ET.QName(lang, "lang")
    # namespace_prefix = "{%s}" % lang
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
            if toolbox_utils.get_toolbox_tag(line) == tag:
                page = ET.SubElement(body, "div", div_attr)
                p_element = ET.SubElement(page, "p")
                ET.SubElement(p_element, "s").text = line
            else:
                ET.SubElement(p_element, "s", no_align_attr).text = line

    tree.write(output, xml_declaration=True, encoding="UTF-8", pretty_print=True)
