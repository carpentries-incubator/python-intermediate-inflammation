#!/usr/bin/env python3
"""Software for managing patient data in our imaginary hospital.

This module is the entry-point to the software, it simply collects
arguments from the command line and passes them to the controller.
"""

import argparse

from inflammation import controller

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient data management system')

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient')

    args = parser.parse_args()

    controller.controller(args)
