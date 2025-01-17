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


class CSVDataSrc:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_data(self):
        csv_file_list = glob.glob(os.path.join(self.data_dir, 'inflammation*.csv'))
        csv_file_list.sort()
        if len(csv_file_list) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.data_dir}")
        print('Loading : ', csv_file_list[0], csv_file_list[-1])
        return map(models.load_csv, csv_file_list)


class JSONDataSrc:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_data(self):
        json_file_list = glob.glob(os.path.join(self.data_dir, 'inflammation*.json'))
        json_file_list.sort()
        if len(json_file_list) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.data_dir}")
        print('Loading : ', json_file_list[0], json_file_list[-1])
        return map(models.load_csv, json_file_list)


def analyse_data(data_dir, src_type=CSVDataSrc):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""

    data = src_type(data_dir).load_data()
    daily_standard_deviation = compute_daily_sdev(data)

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }

    views.visualize(graph_data)