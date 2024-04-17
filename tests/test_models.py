"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest


@pytest.mark.parametrize(
    "test_mean, expected_mean",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [3, 4]),
    ],
)
def test_daily_mean(test_mean, expected_mean):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_mean

    npt.assert_array_equal(daily_mean(np.array(test_mean)), np.array(expected_mean))


@pytest.mark.parametrize(
    "test_max, expected_max",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [5, 6]),
        ([[40, 5], [46, 4], [51, 3]], [51, 5]),
    ],
)
def test_daily_max(test_max, expected_max):
    """Test max function works for array of zeroes and positive integers."""
    from inflammation.models import daily_max

    npt.assert_array_equal(daily_max(np.array(test_max)), np.array(expected_max))


@pytest.mark.parametrize(
    "test_min, expected_min",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [1, 2]),
        ([[40, 5], [46, 4], [51, 3]], [40, 3]),
    ],
)
def test_daily_min(test_min, expected_min):
    """Test min function works for array of zeroes and positive integers."""
    from inflammation.models import daily_min

    npt.assert_array_equal(daily_min(np.array(test_min)), np.array(expected_min))


def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([["Hello", "there"], ["General", "Kenobi"]])


@pytest.mark.parametrize(
    "test_norm, expected_norm",
    [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
        )
    ],
)
def test_patient_normalise(test_norm, expected_norm):
    """Test normalisation works for arrays of one and positive integers.
    Assumption that test accuracy of two decimal places is sufficient."""
    from inflammation.models import patient_normalise

    npt.assert_almost_equal(
        patient_normalise(np.array(test_norm)), np.array(expected_norm), decimal=2
    )


@pytest.mark.parametrize(
    "test_stdev, expected_stdev",
    [
        ([[1, 2], [3, 4], [5, 6]], [1.63, 1.63]),
        ([[40, 5], [46, 4], [51, 3]], [4.50, 0.82]),
    ],
)
def test_daily_stdev(test_stdev, expected_stdev):
    """Test stdev function works for array of zeroes and positive integers."""
    from inflammation.models import daily_stdev

    npt.assert_almost_equal(daily_stdev(np.array(test_stdev)), np.array(test_stdev))
