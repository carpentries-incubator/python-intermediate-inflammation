# Introduction

This project is used to analyse inflammation data, using various data analysis methods. The data is stored in multiple CSV files.

## Exaplanation
There are 3 main folders in this project:
- Data: Stores all the inflammation data as CSV files.
- Inflammation:
    - models.py: loads the patient inflamation.csv data and produces the daily mean, max, min and patient normalisation.
    - views.py: plots patient inflammation.csv data
- Tests:
    - test_models.py: Test the statistical functions with pseudo data
    - test_patient.py: Tests the 'patient' model using a name

As well as this the inflammation-analysis.py is used to manage and analyse patient inflammation data.

## Important information:
requirements.txt - contains the libaries needed for thi project
LICENCE.md

