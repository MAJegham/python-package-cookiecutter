"""tests for is_numeric function from {{cookiecutter.package_name}}.utils.utils"""

from {{cookiecutter.package_name}}.utils.utils import is_numeric


def test_is_numeric_on_negative_float(neg_float):
    assert is_numeric(neg_float)


def test_is_numeric_on_positive_float(pos_float):
    assert is_numeric(pos_float)


def test_is_numeric_on_positive_int(pos_int):
    assert is_numeric(pos_int)


def test_is_numeric_on_negative_int(neg_int):
    assert is_numeric(neg_int)


def test_is_numeric_on_complex(complex_fx):
    assert not is_numeric(complex_fx)


def test_is_numeric_on_list(neg_numbers):
    assert not is_numeric(neg_numbers)


def test_is_numeric_on_string():
    assert not is_numeric("hello")
