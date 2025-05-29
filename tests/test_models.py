"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean, daily_min, daily_max

# the section stating with @ is a decorator, wrapping around the function.
# this shorter function does exactly the same - replaces - the two functions below (test_daily_mean_zeros, test_daily_mean_integers)
@pytest.mark.parametrize(
        "test, expected",
        [
            ([ [0,0], [0,0], [0,0] ], [0,0]), # these are truples (....)
            ([ [1,2], [3,4], [5,6] ], [3,4])
        ]
)
def test_daily_mean(test, expected):
    """Test mean function works for array of zeros and positive integers"""
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_min_integers():
    """Test that the min function works for an array of positive integers."""

    test_input = np.array([[3, 8, 34],
                           [1, 4, 335],
                           [5, 6, 3]])
    test_result = np.array([1, 4, 3])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test_input), test_result)


def test_daily_max_integers():
    """Test that the max function works for an array of positive and negative integers."""

    test_input = np.array([[-3,  8,  83482],
                           [-1, -4, -2],
                           [-5,  6,  89]])
    test_result = np.array([-1, 8, 83482])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)


def test_daily_mean_string():
    """Test for TypeError when passing strings."""

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])