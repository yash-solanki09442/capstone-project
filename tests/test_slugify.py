from src.utils import slugify


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_slugify_trims_spaces():
    assert slugify("  Hello World  ") == "hello-world"


def test_slugify_multiple_spaces():
    assert slugify("Clean   Code") == "clean-code"


def test_slugify_removes_special_chars():
    assert slugify("Hello, World!") == "hello-world"
