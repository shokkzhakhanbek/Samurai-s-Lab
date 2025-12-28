from ascii_art import parse_color, build_mask

def test_parse_named_color():
    assert parse_color("red") == (255, 0, 0)

def test_parse_hex_color():
    assert parse_color("#00ff00") == (0, 255, 0)

def test_parse_rgb_color():
    assert parse_color("rgb(10,20,30)") == (10, 20, 30)

def test_parse_invalid_color():
    assert parse_color("wrong") is None


def test_build_mask_simple():
    result = build_mask("hello", "ll")
    assert result == [False, False, True, True, False]

def test_build_mask_empty_needle():
    result = build_mask("test", "")
    assert result == [True, True, True, True]
