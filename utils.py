from glob import glob
from os import remove
from shutil import rmtree


def cleanup():
    patterns_to_delete = ["calc.fc", "calc.pvd", "cubit*", "outs.csv"]
    to_delete = []
    for pattern in patterns_to_delete:
        to_delete.extend(glob(pattern))
    for item in to_delete:
        remove(item)
    rmtree("calc")
