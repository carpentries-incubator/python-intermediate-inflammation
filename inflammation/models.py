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
    """Calculate the daily mean of a 2D inflammation data array.

    :param data: 2D table of patient data.
    :returns: Mean value of data across all rows, i.e., mean for each patient.
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    :param data: 2D table of patient data.
    :returns: Max value of data across all rows, i.e., max for each patient.
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.

    :param data: 2D table of patient data.
    :returns: Min value of data across all rows, i.e., min for each patient.
    """
    return np.min(data, axis=0)


def standard_deviation(data):
    """Computes and returns standard deviation for data."""
    # Defensive programming
    if not isinstance(data, list):
        raise TypeError("data is not of type list")
    if not all(isinstance(element, (int, float)) for sublist in data for element in sublist):
        raise TypeError("Elements of data are not floats or integers.")
    if any(len(sublist) == 0 for sublist in data):
        raise ValueError("data must not contain empty lists.")

    devs = []
    for row in data:
        devs.append(np.std(row))

    std_dev = sum(devs) / len(data)
    return std_dev
