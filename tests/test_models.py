"""Tests for statistics functions within the Model layer."""

import os
import numpy as np
import numpy.testing as npt
import pytest


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


@pytest.mark.parametrize(
    'data, expected_standard_deviation, expect_raises',
    [
        ([[0, 0, 0]], 0.0, None),
        ([[1.0, 1.0, 1.0]], 0, None),
        ([[0., 2.]], 1., None),
        ([[0.0, 2.0]], 0.0, AssertionError),
        ([[-1, -1, -1]], 0.0, None),
        ("A string", None, TypeError),
        ([[]], None, ValueError),
        ([["List", "of", "strings"]], None, TypeError),
        ([[0., 2.], [1., 1.]], 0.5, None)

    ],
    ids=["Good test with 0s", "Good test with 1s", "Good test, varying values", "Raises AssertionError",
         "Good test with negative values", "Raises TypeError, input is string", "Raises ValueError, empty input",
         "Raises TypeError, input is list of strings", "Test with multiple rows in data"])
def test_daily_standard_deviation(data, expected_standard_deviation, expect_raises):
    from inflammation.models import standard_deviation

    if expect_raises is not None:
        with pytest.raises(expect_raises):
            result_data = standard_deviation(data)
            npt.assert_array_equal(result_data, expected_standard_deviation)

    else:
        result_data = standard_deviation(data)
        npt.assert_array_equal(result_data, expected_standard_deviation)


