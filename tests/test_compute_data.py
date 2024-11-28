from unittest.mock import Mock
import glob
import os
from inflammation import models

def test_computer_data_mock_source():
    from inflammation.compute_data import analyse_data
    data_source = Mock()

    #TODO - create mock data to pass---------------

    data_dir = "data/" #could have a different folder of mock data
    data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.csv'))

    if len(data_file_paths) == 0:
        raise ValueError(f"No inflammation data CSV files found in path {self.dir_path}")

    data_loc = map(models.load_csv, data_file_paths)
    mock_data = list(data_loc)

    data_source.method_to_mock.return_value = mock_data

    #----------------------------------------------


    #TODO