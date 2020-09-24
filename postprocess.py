import csv
from math import sqrt

from paraview import servermanager
from paraview.simple import *


def get_mean_component(array, component_index):
    array_length = array.GetNumberOfTuples()
    return (
        sum(array.GetComponent(i, component_index) for i in range(array_length))
        / array_length
    )


reader = PVDReader(FileName=r"C:\Projects\effective_yield_surface\calc.pvd")
data = servermanager.Fetch(reader)
point_data = data.GetPointData()

stress = point_data.GetArray("Stress")

averaged_stress = [
    [get_mean_component(stress, 0), get_mean_component(stress, 3)],
    [get_mean_component(stress, 3), get_mean_component(stress, 1)],
]
principial_averaged_stress = [
    (averaged_stress[0][0] + averaged_stress[1][1]) / 2
    + sqrt(
        ((averaged_stress[0][0] - averaged_stress[1][1]) / 2) ** 2
        + averaged_stress[0][1] ** 2
    ),
    (averaged_stress[0][0] + averaged_stress[1][1]) / 2
    - sqrt(
        ((averaged_stress[0][0] - averaged_stress[1][1]) / 2) ** 2
        + averaged_stress[0][1] ** 2
    ),
]
with open("outs.csv", "a+") as outs:
    outs.write(
        "{},{}\n".format(principial_averaged_stress[0], principial_averaged_stress[1])
    )
    outs.write(
        "{},{}\n".format(principial_averaged_stress[1], principial_averaged_stress[0])
    )
