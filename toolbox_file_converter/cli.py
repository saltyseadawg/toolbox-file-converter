import click


@click.command()
@click.option("-f", "--filename", required=True)
@click.option("-o", "--output", required=True)
@click.option("-t", "--tag", required=True)
def convert(filename, output, tag):
    """
    Converts in_file into an xml out_file for Readalongs Studio.
    Exclude_tags are converted into xml objects that won't be aligned.
    """

    # Assuming that only one tag will be aligned
    pass
