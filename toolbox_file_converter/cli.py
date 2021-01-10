import click

import text_utils

DO_NOT_ALIGN_TAG = 'do-not-align'

@click.command()
@click.option("-f", "--toolboxfile", required=True)
@click.option("-o", "--output", required=True)
@click.option("-t", "--tag", required=True)
@click.option("-l", "--language", required=True)
def convert(filename, output, tag):
    """
    Converts in_file into an xml out_file for Readalongs Studio.
    Exclude_tags are converted into xml objects that won't be aligned.
    """
    root = ET.Element('TEI')
    # Assuming that only one tag will be aligned
    with open(filename) as fp:

        lines = fp.readlines()
        for line in lines:
            if not text_utils.get_toolbox_tag(line)
                continue
            
