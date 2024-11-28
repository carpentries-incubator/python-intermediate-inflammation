"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views

class CSVDataSource:
    """Loads data from specified directory path and returns list of 2D NumPy arrays"""

    def __init__(self,dir_path):
        self.dir_path = dir_path

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.dir_path}")
        data = map(models.load_csv, data_file_paths)

        return list(data)
    
class JSONDataSource:
    """
    Loads patient data with inflammation values from JSON files within a specified folder.
    """
    
    def __init__(self,dir_path):
        self.dir_path = dir_path

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data JSON files found in path {self.dir_path}")
        data = map(models.load_json, data_file_paths)

        return list(data)


def analyse_data(data_source):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""

    data = data_source.load_inflammation_data()

    # means_by_day = map(models.daily_mean, data)
    # means_by_day_matrix = np.stack(list(means_by_day))

    # daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    # graph_data = {
    #     'standard deviation by day': daily_standard_deviation,
    # }
    # views.visualize(graph_data)
    daily_standard_deviation = compute_standard_deviation_by_data(data)

    return daily_standard_deviation
    print("Test")