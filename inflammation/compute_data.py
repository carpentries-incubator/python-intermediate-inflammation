"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views


class Data_Loader:
    def __init__(self, data_dir):
        self.data_dir = data_dir 

    def load_inflammation_data(self):
        """Loads all inflammation data from CSV files within a directory.
        :return: A list of numpy arrays containing the inflammation data.
        """
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.csv'))
        if len(data_file_paths) == 0:       
            raise ValueError(f"No inflammation data CSV files found in path {self.data_dir}")
    
        if not all(os.path.isfile(path) for path in data_file_paths):
            raise ValueError(f"Not all files in {self.data_dir} are valid files.")
        data = map(models.load_csv, data_file_paths)
        data = list(data)  # Convert map object to a list of numpy arrays

        return data 




def analyse_data():
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""

    data_source = Data_Loader(data_dir)
    data = data_source.load_inflammation_data()


    means_by_day = [models.daily_mean(d) for d in data]
    means_by_day_matrix = np.stack(means_by_day)

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    views.visualize(graph_data)



