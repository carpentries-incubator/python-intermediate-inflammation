"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.

Functions:
    load_csv - return a Numpy array from CSV file
    daily_mean - returns the mean of a Numpy array
    daily_max - returns the max of a Numpy array
    daily_min - returns the min of a Numpy array
    daily_std - returns the standard deviation of a Numpy array
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    :returns: Numpy array
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array for each day.

   :param data: A 2D data array with inflammation data
   (each row contains measurements for a single patient across all days).
   :returns: An array of mean values of measurements for each day.
   """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily maximum of a 2D inflammation data array for each day.

   :param data: A 2D data array with inflammation data
   (each row contains measurements for a single patient across all days).
   :returns: An array of max values of measurements for each day.
   """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily minimum of a 2D inflammation data array for each day.

   :param data: A 2D data array with inflammation data
   (each row contains measurements for a single patient across all days).
   :returns: An array of minimum values of measurements for each day.
   """
    return np.min(data, axis=0)


def daily_std(data):
    """Calculate the daily standard deviation of a 2D inflammation data array for each day.

   :param data: A 2D data array with inflammation data
   (each row contains measurements for a single patient across all days).
   :returns: An array of daily standard deviation measurements for each day.
   """
    return np.std(data, axis=0)


def patient_normalise(data):
    """
    Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0.

    Negative values are rounded to 0.
    """
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')

    max_data = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max_data[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised
