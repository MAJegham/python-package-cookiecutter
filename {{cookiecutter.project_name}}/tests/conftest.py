"""Basic fixtures"""

import pytest


@pytest.fixture
def pos_float():
    return 1009.3


@pytest.fixture
def neg_float():
    return -15.6


@pytest.fixture
def pos_int():
    return 10


@pytest.fixture
def neg_int():
    return -112


@pytest.fixture
def complex_fx():
    return 1 + 15j


@pytest.fixture
def neg_numbers():
    return [-1.0256e4, -1548.25, -52.9487, -15, -8.6]


@pytest.fixture
def pos_numbers():
    return [48.25, 52.9487, 151.5, 488.6, 1.0256e7]
