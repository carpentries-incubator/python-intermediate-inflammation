"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt

from inflammation.models import daily_mean, daily_max, daily_min

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

def test_daily_max():
    """Test that max function works for an array of positive integers."""

    test_input = np.array([[4, 2, 5],
                           [1, 6, 2],
                           [4, 1, 9]])
    test_result = np.array([4, 6, 9])

    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_min():
    """Test that max function works for an array of positive integers."""

    test_input = np.array([[4, 2, 5],
                           [1, 6, 2],
                           [4, 1, 9]])
    test_result = np.array([1, 1, 2])

    npt.assert_array_equal(daily_min(test_input), test_result)