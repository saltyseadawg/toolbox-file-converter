import click

import text_utils

DO_NOT_ALIGN_TAG = 'do-not-align'

@click.command()
@click.option("-f", "--toolboxfile", required=True)
@click.option("-o", "--output", required=True)
@click.option("-t", "--tag", required=True)
@click.option("-l", "--lang", required=True)
def convert(filename, output, tag, lang):
    """
    Converts in_file into an xml out_file for Readalongs Studio.
    Exclude_tags are converted into xml objects that won't be aligned.
    """
    readalongs_attr = {
        'xml:lang': lang
    }

    div_attr = {
        'type': 'page'
    }

    root = ET.Element('TEI')
    text = ET.SubElement(parent=root, tag='text', attrib=readalongs_attr)
    body = ET.SubElement(parent=text, tag='body')
    div = ET.SubElement(parent=body, tag='div', attrib=div_attr)

    # Assuming that only one tag will be aligned
    with open(filename) as fp:

        lines = fp.readlines()
        for line in lines:
            if not text_utils.get_toolbox_tag(line)
                continue
            
