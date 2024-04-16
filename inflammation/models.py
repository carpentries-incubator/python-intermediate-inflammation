"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """
    Calculate the daily mean of a 2D inflammation data array.

    :param data: 2D inflammation data array
    returns: daily mean
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """
    Calculate the daily max of a 2D inflammation data array.

    :param data: 2D inflammation data array
    returns: daily max
    """
    return np.max(data, axis=0)


def daily_min(data):
    """
    Calculate the daily min of a 2D inflammation data array.

    :param data: 2D inflammation data array
    returns: daily min
    """
    return np.min(data, axis=0)


def patient_normalise(data):
    """
    Normalise patient data from a 2D inflammation data array.
    NaN values are ignored, and normalised to 0.
    Negative values are rounded to 0.

    :param data: 2D inflammation data array
    :returns: normalised patient data
    """
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')
    if not isinstance(data, np.ndarray):
        raise TypeError('Inflammation data should be an Numpy nd-array')

    max_val = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max_val[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised
