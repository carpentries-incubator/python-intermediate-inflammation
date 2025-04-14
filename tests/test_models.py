"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean, daily_max, daily_min
from inflammation.models import patient_normalise


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0,0],[0,0],[0,0]],[0,0]),
        ([[0, 0],[0, 0],[0, 0]], [0, 0]),
        ([[-1, -1],[-1, -1],[-1, -1]],[-1, -1]),
        ([[1, 2],[3, 4],[5, 6]],[3, 4]),
        ([[1, 2],[3, 4],[5, 6]], [6, 7])
    ]
)
#not sure why pytest seems to be required here. error says it should be test but doesn't seem to work
def pytest_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)
#------------------------------------------
def test_daily_mean_negatives():
    """Test that mean function works for an array of zeros."""

    test_input = np.array([[-1, -1],
                           [-1, -1],
                           [-1, -1]])
    test_result = np.array([-1, -1])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)
#------------------------------------------

def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_mean():
    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    npt.assert_array_equal(daily_mean(test_input), test_result)
"""
def test_daily_mean_string():
    test_input = np.array([["this is something incorrect", 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    npt.assert_array_equal(daily_mean(test_input), test_result)
"""


"""
def test_daily_min_string():
    #test for typeerror when passing strings

    #with pytest.raises(TypeError):
     #   error_expected = daily_min([["one", "two"],["3","4"]])
"""



@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]])
    ])
def test_patient_normalise(test, expected):
    """Test normalisation works for arrays of one and positive integers.
       Test with a relative and absolute tolerance of 0.01."""

    result = patient_normalise(np.array(test))
    npt.assert_allclose(result, np.array(expected), rtol=1e-2, atol=1e-2)


#this is an update test

"""Tests for the Patient model - class/file in this folder

from inflammation.models import Patient

def test_create_patient():

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name
"""