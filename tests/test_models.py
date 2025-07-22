"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt

from inflammation.models import daily_mean

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





import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from inflammation.compute_data import load_inflammation_data, analyse_data


def test_load_inflammation_data():   
    """Test that load_inflammation_data loads data correctly."""
    
    # Assuming the data directory is 'data' and contains valid CSV files    
    data_dir = 'data'
    data = load_inflammation_data(data_dir)

    # Check that data is a list of numpy arrays 
    assert isinstance(data, list)
    assert all(isinstance(d, np.ndarray) for d in data)
    

