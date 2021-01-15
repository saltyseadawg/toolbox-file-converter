from toolbox_file_converter import toolbox_utils as tu

def test_get_toolbox_tag():
    simple_tag = r'\x some text'
    assert tu.get_toolbox_tag(simple_tag) == 'x'

    no_tag = ''
    assert tu.get_toolbox_tag(no_tag) == None

    longer_tag = r'\longtag some text'
    assert tu.get_toolbox_tag(longer_tag) == 'longtag'

