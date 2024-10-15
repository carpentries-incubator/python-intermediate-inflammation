"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views


def load_inflammation_data(dir_path):
    data_file_paths = glob.glob(os.path.join(dir_path, 'inflammation*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError(f"No inflammation CSV files found in path {dir_path}")
    data = map(models.load_csv, data_file_paths) # Load inflammation data from each CSV file
    return list(data) # Return the list of 2D NumPy arrays with inflammation data

def analyse_data(data_dir):
    data = load_inflammation_data(data_dir)

    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    views.visualize(graph_data)