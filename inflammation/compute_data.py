"""Module containing mechanism for calculating standard deviation between datasets.
"""

from typing import List
import glob
import os
import numpy as np
from pathlib import Path

from inflammation import models, views


class JSONDataSource:
    def __init__(self, data_dir: Path):
        '''Constructor method for JSONDataSource.

        Takes in data_dir argument on construction.

        Parameters
        ----------
        data_dir : Path
            The full path to the directory where your inflammation CSV files are stored.

        Returns
        -------
        None
        '''
        self.data_dir = data_dir

    def load_inflammation_data(self) -> List[np.ndarray]:
        '''Loads the inflammation data into the class.
        '''

        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data JSON files found in path {self.data_dir}")
        data = list(map(models.load_json, data_file_paths))

        return data

class CSVDataSource:
    def __init__(self, data_dir: Path):
        '''Constructor method for CSVDataSource.

        Takes in data_dir argument on construction.

        Parameters
        ----------
        data_dir : Path
            The full path to the directory where your inflammation CSV files are stored.

        Returns
        -------
        None
        '''
        self.data_dir = data_dir

    def load_inflammation_data(self) -> List[np.ndarray]:
        '''Loads the inflammation data into the class.
        '''

        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.data_dir}")
        data = list(map(models.load_csv, data_file_paths))

        return data

