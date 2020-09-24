import os
import subprocess
import sys

from config import (
    FIDESYS_BASE_FOLDER,
    FIDESYS_CALC,
    FIDESYS_LIBPATH,
    FIDESYS_PYTHONPATH,
)

for subpath in FIDESYS_PYTHONPATH:
    sys.path.append(FIDESYS_BASE_FOLDER + subpath)
os.environ["PATH"] = (
    ";".join(FIDESYS_BASE_FOLDER + subpath for subpath in FIDESYS_LIBPATH)
    + ";"
    + os.environ.get("PATH", "")
)
import cubit  # isort:skip
from fidesys import FidesysComponent  # isort:skip

displacement_x, displacement_y = sys.argv[1], sys.argv[2]

with open("template_2d.txt") as template:
    script = (
        template.read()
        .format(displacement_x=displacement_x, displacement_y=displacement_y)
        .split("\n")
    )


cubit.init([""])
fc = FidesysComponent()
fc.start_up_no_args()

for command in script:
    cubit.cmd(command)
fc.writeFC(r"C:\Projects\effective_yield_surface\calc.fc", True)
subprocess.call(
    [
        FIDESYS_CALC,
        r"--input=C:\Projects\effective_yield_surface\calc.fc",
        r"--output=C:\Projects\effective_yield_surface\calc.pvd",
    ]
)
cubit.destroy()
