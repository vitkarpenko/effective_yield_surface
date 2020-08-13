from glob import glob
from os import remove
from os.path import isdir, isfile
from shutil import rmtree


def cleanup(start=False):
    patterns_to_delete = ["calc.fc", "calc.pvd", "cubit*"]
    to_delete = []
    for pattern in patterns_to_delete:
        to_delete.extend(glob(pattern))
    for item in to_delete:
        remove(item)
    if isdir("calc"):
        rmtree("calc")
    if start and isfile("outs.csv"):
        remove("outs.csv")
