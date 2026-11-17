"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np
from dataclasses import dataclass

from inflammation import models, views

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
        data = map(models.load_csv, data_file_paths)
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
        data = map(models.load_json, data_file_paths)
        return list(data)


def compute_standard_deviation_by_day(data):
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    return daily_standard_deviation

def analyse_data(data_source):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""

    data = data_source.load_inflammation_data()
    daily_standard_deviation = compute_standard_deviation_by_day(data)

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    return graph_data
    # views.visualize(graph_data)