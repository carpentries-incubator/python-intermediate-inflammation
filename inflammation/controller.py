"""Module containing the MVC Controller of the patient data system."""

from inflammation import (patient, plotting)


def controller(args):
    """The MVC Controller of the patient data system.
    
    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    infiles = args.infiles
    if not isinstance(infiles, list):
        infiles = [args.infiles]

    for filename in infiles:
        inflammation_data = patient.load_csv(filename)
        plotting.visualize(inflammation_data)
