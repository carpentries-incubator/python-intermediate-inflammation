"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views

def load_information_data(dir_path):
    """Load all inflammantion*.csvfiles from dir_path""" 
    data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError(f"No inflammation data CSV files found in path {data_dir}")

    data = map(models.load_csv, data_file_paths)
    return list(data)


def analyse_data(data_dir):
    """Calculates the standard deviation by day between datasets."""
    data = load_inflammation_data(data_dir)

    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    views.visualize(graph_data)