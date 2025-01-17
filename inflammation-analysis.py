#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import argparse
import os

from inflammation import models, views
from inflammation.compute_data import analyse_data
from inflammation.compute_data import CSVDataSrc, JSONDataSrc

def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    infiles = args.infiles
    if not isinstance(infiles, list):
        infiles = [args.infiles]


    if args.full_data_analysis:
        data_src = os.path.dirname(infiles[0])
        _, data_ext = os.path.splitext(infiles[0])
        if data_ext == ".csv":
            src_type = CSVDataSrc
        elif data_ext == ".json":
            src_type = JSONDataSrc
        else:
            raise ValueError('Unknown extension: {data_ext}')
        analyse_data(data_src, src_type=src_type)
        return

    for filename in infiles:
        inflammation_data = models.load_csv(filename)

        view_data = {
            'average': models.daily_mean(inflammation_data),
            'max': models.daily_max(inflammation_data),
            'min': models.daily_min(inflammation_data)
        }

        views.visualize(view_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient inflammation data management system')

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient')

    parser.add_argument(
        '--full-data-analysis',
        action='store_true',
        dest='full_data_analysis')

    args = parser.parse_args()

    main(args)
