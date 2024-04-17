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
    return np.loadtxt(fname=filename, delimiter=",")


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    :param data: 2D inflammation data array.
    :returns: An array of mean values of measurements for each day.
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    :param data: 2D inflammation data array.
    :returns: An array of mean values of measurements for each day.
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.

    :param data: 2D inflammation data array.
    :returns: An array of mean values of measurements for each day.
    """
    return np.min(data, axis=0)


def patient_normalise(data):
    """Normalise patient data from a 2D inflammation data array.

    :param data: 2D inflammation data array.
    :returns: An array of normalized values of measurements for each day.
    """
    max = np.max(data, axis=1)
    return data / max[:, np.newaxis]


def daily_stdev(data):
    """Calculate the daily standard deviation of a 2D inflammation data array.

    :param data: 2D inflammation data array.
    :returns: An array of std values of measurements for each day.
    """
    std = np.std(data, axis=0)
    return std
