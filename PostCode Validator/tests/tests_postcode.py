import pytest
import PostCodeValidator

@pytest.mark.parametrize("postcode, expected", [
    ("SW1A 1AA", True),
    ("W1A 1HQ", True),
    ("EC1A 1BB", True),
    ("BFPO 1234", True),
    ("BFPO 1234AB", True),
    ("BFPO 012", False),
    ("ABCDE 1234", False),
    ("SW1A 1AA ", False),
    ("W1A1HQ", False),
    ("1234 5678", False),
    ("AB1 1AA", True)
])
def test_post_code_valid(postcode, expected):
    assert PostCodeValidator.post_code_valid(PostCodeValidator.combinedPattern, postcode) == expected


@pytest.mark.parametrize("postcode, expected", [
    ("   SW1A 1AA    ", "SW1A 1AA"),
    ("SW1A 1AA     ", "SW1A 1AA"),
    ("     SW1A 1AA", "SW1A 1AA"),
])
def test_strip_trailing_spaces_postcode(postcode, expected):
    assert PostCodeValidator.strip_trailing_spaces_postcode(postcode) == expected

@pytest.mark.parametrize("postcode, expected", [
    ("$W1A 1@@", "W1A 1"),
    ("!@£# ()-%$==", " "),
    ("--- 1AA", " 1AA"),
])
def test_remove_special_chars(postcode, expected):
    assert PostCodeValidator.remove_special_chars(postcode) == expected

@pytest.mark.parametrize("postcode, expected", [
    ("sw1A 1aa", "SW1A 1AA"),
    ("Sw1a 1aA", "SW1A 1AA"),
    ("sw1a 1AA", "SW1A 1AA"),
])
def test_format_postcode_to_upper_text(postcode, expected):
    assert PostCodeValidator.format_postcode_to_upper_text(postcode) == expected