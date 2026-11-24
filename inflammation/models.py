"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains
inflammation data for a single patient taken over a number of days
and each column represents a single day across all patients.
"""
import json
import glob
import os

import numpy as np

from dataclasses import dataclass

def load_csv(filename: str) -> np.ndarray:
    """Load a Numpy array from csv

        Parameters
        ----------
        filename : str
            path to the csv file

        Returns
        -------
        np.ndarray
            2D array of inflammation data
    """
    return np.loadtxt(fname=filename, delimiter=",")


def load_json(filename):
    """Load a numpy array from a JSON document.

    Expected format:
    [
      {
        "observations": [0, 1]
      },
      {
        "observations": [0, 2]
      }
    ]
    :param filename: Filename of CSV to load
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data_as_json = json.load(file)
        return [np.array(entry['observations']) for entry in data_as_json]

@dataclass
class CSVDataSource:
    """
    :param data_dir: Directory containing the inflammation data files
    :type data_dir: str
    :param filename_pattern: Glob pattern for inflammation data file names, defaults to "inflammation*.csv"
    :type filename_pattern: str, optional
    """
    data_dir: str
    filename_pattern: str="inflammation*.csv"

    def load_inflammation_data(self) -> np.array:
        """Loads inflammation data from csv files and returns a list of 2D numpy arrays containing the inflammation data

        :raises ValueError: If the data dir does not contain any inflammation data
        :return: Inflammation data per file loaded into a list of numpy arrays.
        :rtype: np.array
        """
        data_file_paths = glob.glob(os.path.join(self.data_dir, self.filename_pattern))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.data_dir}")
        data = map(load_csv, data_file_paths)
        return list(data)



@dataclass
class JSONDataSource:
    """
    :param data_dir: Directory containing the inflammation data files
    :type data_dir: str
    :param filename_pattern: Glob pattern for inflammation data file names, defaults to "inflammation*.json"
    :type filename_pattern: str, optional
    """
    data_dir: str
    filename_pattern: str="inflammation*.json"

    def load_inflammation_data(self) -> np.array:
        """Loads inflammation data from json files and returns a list of 2D numpy arrays containing the inflammation data

        :raises ValueError: If the data dir does not contain any inflammation data
        :return: Inflammation data per file loaded into a list of numpy arrays.
        :rtype: np.array
        """
        data_file_paths = glob.glob(os.path.join(self.data_dir, self.filename_pattern))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data JSON files found in path {self.data_dir}")
        data = map(load_json, data_file_paths)
        return list(data)



def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    :param data: 2D data inflammation array, with one row per patient
    :type data: numpy.Array (2D)
    :return: The mean inflammation for each patient
    :rtype: numpy.Array (1D)
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    :param data: 2D data inflammation array, with one row per patient
    :type data: numpy.Array (2D)
    :return: The maximum inflammation for each patient
    :rtype: numpy.Array (1D)
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.

    :param data: 2D data inflammation array, with one row per patient
    :type data: numpy.Array (2D)
    :return: The minimum inflammation for each patient
    :rtype: numpy.Array (1D)
    """
    return np.min(data, axis=0)


def patient_normalise(data):
    """Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0.

    Negative values are rounded to 0.

    :param data: 2D data inflammation array, with one row per patient
    :type data: numpy.Array (2D)
    :raises ValueError: If any of the values are negative we cannot normalize.
    :raises TypeError: If the data are not an ndarray
    :return: The normalized inflammation for each patient
    :rtype: numpy.Array (1D)
    """
    if not isinstance(data, np.ndarray):
        raise TypeError('Inflammation values should be an np.ndarray')
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')

    max_values = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max_values[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised

def compute_standard_deviation_by_day(data):
    means_by_day = map(daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    return daily_standard_deviation
