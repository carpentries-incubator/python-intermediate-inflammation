"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV"""
    return np.loadtxt(fname=filename, delimiter=',')


# TODO(lesson-design) Add Patient class
# TODO(lesson-design) Implement data persistence
