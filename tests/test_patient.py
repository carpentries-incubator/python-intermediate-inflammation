"""Tests for the Patient model."""

from inflammation.models import Patient

def test_create_patient():

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name
