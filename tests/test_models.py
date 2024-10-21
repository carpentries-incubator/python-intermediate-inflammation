"""Tests for statistics functions within the Model layer."""
# pylint: disable=C0415

import numpy as np
import numpy.testing as npt
import pytest


@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))


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


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1, 2], [3, 4], [5, 6]], [5, 6]),
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[0, 1, 2], [3, 4, 10], [6, 7, 8]], [6, 7, 10]),
    ])
def test_daily_max(test, expected):
    """Test that max function works various arrays."""
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1, 2], [3, 4], [5, 6]], [1, 2]),
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[0, 1, 2], [3, 4, -5], [6, 7, 8]], [0, 1, -5]),
        ([[0, -8, 2], [3, 4, -5], [6, 7, 8]], [0, -8, -5]),
    ])
def test_daily_min(test, expected):
    """Test that min function works various arrays."""
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))


def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        daily_min([['Hello', 'there'], ['General', 'Kenobi']])
