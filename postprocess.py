import csv
from math import sqrt

from paraview import servermanager
from paraview.simple import *

YIELD_STRENGTH = 1.6e8


def get_mean_component(array, component_index):
    array_length = array.GetNumberOfTuples()
    return sum(array.GetComponent(i, component_index) for i in range(array_length)) / array_length


def get_max_component(array, component_index):
    array_length = array.GetNumberOfTuples()
    return max(array.GetComponent(i, component_index) for i in range(array_length))


reader = PVDReader(FileName=r"C:\Projects\effective_yield_surface\calc.pvd")
data = servermanager.Fetch(reader)
point_data = data.GetPointData()

stress = point_data.GetArray("Stress")
max_mises_stress = get_max_component(stress, 6)
scale_coefficient = YIELD_STRENGTH / max_mises_stress

averaged_stress = [
    [get_mean_component(stress, 0), get_mean_component(stress, 3)],
    [get_mean_component(stress, 3), get_mean_component(stress, 1)],
]
principial_averaged_stress = [
    (averaged_stress[0][0] + averaged_stress[1][1]) / 2
    + sqrt(((averaged_stress[0][0] - averaged_stress[1][1]) / 2) ** 2 + averaged_stress[0][1] ** 2),
    (averaged_stress[0][0] + averaged_stress[1][1]) / 2
    - sqrt(((averaged_stress[0][0] - averaged_stress[1][1]) / 2) ** 2 + averaged_stress[0][1] ** 2),
]
with open("outs.csv", "a+") as outs:
    outs.write(
        "{},{}\n".format(
            principial_averaged_stress[0] / YIELD_STRENGTH * scale_coefficient,
            principial_averaged_stress[1] / YIELD_STRENGTH * scale_coefficient,
        )
    )
    outs.write(
        "{},{}\n".format(
            principial_averaged_stress[1] / YIELD_STRENGTH * scale_coefficient,
            principial_averaged_stress[0] / YIELD_STRENGTH * scale_coefficient,
        )
    )
