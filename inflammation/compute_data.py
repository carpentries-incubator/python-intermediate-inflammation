"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views


def compute_sdev(data, axis=0):
    """
    Compute standard deviation
    """
    return np.std(data, axis=axis)


def compute_stacked_means_by_day(data):
    """
    Apply models.daily_mean to data and np.stack them.
    """
    means_by_day = map(models.daily_mean, data)
    return np.stack(list(means_by_day))


def compute_daily_sdev(data):
    means_by_day_matrix = compute_stacked_means_by_day(data)
    return compute_sdev(means_by_day_matrix)


class CSVStuff:
    def __init__(self, csv_file_list):
        self.csv_filenames = csv_file_list

    def load_data(self):
        return map(models.load_csv, self.csv_filenames)


def analyse_data(data_dir):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""

    data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError(f"No inflammation data CSV files found in path {data_dir}")

    data = CSVStuff(data_file_paths).load_data()
    daily_standard_deviation = compute_daily_sdev(data)

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }

    views.visualize(graph_data)