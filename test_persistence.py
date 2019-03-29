from persistence import *
import pytest


def test_multiply():
    assert 6 == multiply([3, 2, 1])


@pytest.mark.parametrize("expected, input", [(0, 1), (1, 14), (2, 25), (3, 39)])
def test_persistence(expected, input):
    assert expected == persistence(input)


@pytest.mark.parametrize("expected, input", [(1, 1), (2, 14), (3, 225), (5, 12345)])
def test_length_number(expected, input):
    assert expected == length_number(input)


@pytest.mark.parametrize("expected, input",
                         [
                             ([3, 2, 3], 323),
                             ([1, 2, 5, 7], 1257),
                             ([9, 8, 6], -986),
                             ([3], 3)
                         ])
def test_listifier(expected, input):
    assert expected == listifier(input)