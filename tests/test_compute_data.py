'''Module for testing compute data functions.'''
from unittest.mock import Mock
import pytest
import math
import numpy as np
import numpy.testing as npt
from pathlib import Path

@pytest.mark.parametrize(
    "test, expect_returns, raises_AssertionError",
    [
        (
            [np.array([1, 2, 3, 4, 5])],
            np.array([0, 0, 0, 0, 0]),
            False
         ),
        (
            [np.array([1, 2, 3, 4, 5]),
             np.array([1, 2, 3, 4, 5]),
             np.array([1, 2, 3, 4, 5])],
            np.array([0, 0, 0, 0, 0]),
            False
        ),
        (
            [np.array([1, 2, 3, 4, 5])],
            np.array([0, 0, 0, 0, 1]),
            True
        )
    ],
    ids=['One patient in one file',
         'One patient in three files',
         'One patient in one file, but incorrect expected_returns.']
)
def test_compute_standard_deviation_by_day(test, expect_returns, raises_AssertionError):
    from inflammation.models import compute_standard_deviation_by_day

    if raises_AssertionError:
        with pytest.raises(AssertionError):
            result = compute_standard_deviation_by_day(test)
            npt.assert_array_equal(result, expect_returns)

    else:
        result = compute_standard_deviation_by_day(test)
        npt.assert_array_equal(result, expect_returns)



def test_analyse_data():
    from inflammation.models import analyse_data
    from inflammation.compute_data import CSVDataSource
    path = Path.cwd() / "../data"
    data_source = CSVDataSource(path)
    result = analyse_data(data_source)

    expected_output = [0., 0.22510286, 0.18157299, 0.1264423, 0.9495481, 0.27118211,
                       0.25104719, 0.22330897, 0.89680503, 0.21573875, 1.24235548, 0.63042094,
                       1.57511696, 2.18850242, 0.3729574, 0.69395538, 2.52365162, 0.3179312,
                       1.22850657, 1.63149639, 2.45861227, 1.55556052, 2.8214853, 0.92117578,
                       0.76176979, 2.18346188, 0.55368435, 1.78441632, 0.26549221, 1.43938417,
                       0.78959769, 0.64913879, 1.16078544, 0.42417995, 0.36019114, 0.80801707,
                       0.50323031, 0.47574665, 0.45197398, 0.22070227]
    npt.assert_array_almost_equal(result, expected_output)


def test_compute_data_mock_source():
    from inflammation.compute_data import analyse_data

    data_source = Mock()
    data_source.load_inflammation_data.return_value = [
        [[0, 2, 0]],
        [[0, 1, 0]]
    ]

    result = analyse_data(data_source)

    npt.assert_array_almost_equal(result, [0, math.sqrt(0.25), 0])
