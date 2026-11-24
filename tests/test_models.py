"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean, daily_max, daily_min, patient_normalise


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""

    test_input = np.array([[0, 0], [0, 0], [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2], [3, 4], [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


@pytest.mark.parametrize(
    "input, output",
    [
        [[[1]], [1]],
        [[[1, 2, 3]], [1, 2, 3]],
        [[[0, 0, 0], [1, 2, 3]], [1, 2, 3]],
        [[[1, 2.0, 3.000000000000000001]], [1, 2, 3]],
    ],
)
def test_daily_max(input, output):
    test_input = np.array(input)
    test_result = np.array(output)
    npt.assert_array_equal(daily_max(test_input), test_result)


@pytest.mark.parametrize(
    "input, output",
    [
        [[[1]], [1]],
        [[[1, 2, 3]], [1, 2, 3]],
        [[[0, 0, 0], [1, 2, 3]], [0, 0, 0]],
        [[[1, 2.0, 3.000000000000000001]], [1, 2, 3]],
    ],
)
def test_daily_min(input, output):
    test_input = np.array(input)
    test_result = np.array(output)
    npt.assert_array_equal(daily_min(test_input), test_result)


def test_daily_min_string():
    """Test for TypeError when passing strings"""
    with pytest.raises(TypeError):
        error_expected = daily_min([["Hello", "there"], ["General", "Kenobi"]])


@pytest.mark.parametrize(
    "test, expected, expect_raises",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], None),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]], None),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            None,
        ),
        (
            [[-1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            ValueError,
        ),
        (
            "hello",
            None,
            TypeError
        )
    ],
)
def test_patient_normalise(test, expected, expect_raises):
    """Test normalisation works for arrays of one and positive integers.
    Test with a relative and absolute tolerance of 0.01."""
    if isinstance(test, list):
        test = np.array(test)
    if expect_raises:
        with pytest.raises(expect_raises):
            result = patient_normalise(test)
    else:
        result = patient_normalise(test)
        npt.assert_allclose(result, np.array(expected), rtol=1e-2, atol=1e-2)
