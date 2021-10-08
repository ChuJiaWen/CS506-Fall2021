import pytest
import random

from cs506 import matrix


def test_determinant():
    try:
        matrix.get_determinant([])
    except ValueError as e:
        assert str(e) == "To calculate the determinant the matrix must at least be 2x2"
    try:
        matrix.get_determinant([[0], [0,0]])
    except ValueError as e:
        assert str(e) == "To calculate the determinant the matrix must be square"

    assert matrix.get_determinant([[1,2],[3,4]]) == -2
    assert matrix.get_determinant([[1,2,3],[2,3,4],[4,5,6]]) == 0
    assert matrix.get_determinant([[1,3,2],[4,1,3],[2,5,2]]) == 17
