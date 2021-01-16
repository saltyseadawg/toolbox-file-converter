from toolbox_file_converter import toolbox_utils as tu


def test_get_toolbox_tag():
    simple_tag = r"\x some text"
    assert tu.get_toolbox_tag(simple_tag) == "x"

    no_tag = ""
    assert tu.get_toolbox_tag(no_tag) is None

    longer_tag = r"\longtag some text"
    assert tu.get_toolbox_tag(longer_tag) == "longtag"


def test_remove_tag():
    simple_tag = "x"
    test_line = r"\x some text"
    assert tu.remove_tag(test_line, simple_tag) == "some text"

    no_tag = ""
    assert tu.remove_tag(test_line, no_tag) == test_line
