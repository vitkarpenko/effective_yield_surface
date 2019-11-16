from config import (
    FIDESYS_BASE_FOLDER,
    FIDESYS_CALC,
    FIDESYS_COM_PATH,
    FIDESYS_LIBPATH,
    FIDESYS_PYTHONPATH,
    FIDESYS_VERSION,
    PVPYTHON
)
import os
import sys

for subpath in FIDESYS_PYTHONPATH:
    sys.path.append(FIDESYS_BASE_FOLDER + subpath)

os.environ["PATH"] = (
    ";".join(FIDESYS_BASE_FOLDER + subpath for subpath in FIDESYS_LIBPATH)
    + ";"
    + os.environ.get("PATH", "")
)

import subprocess
from fidesys import FidesysComponent
import cubit

# displacement_x = 0.1
# displacement_y = 0.1

# with open("template_2d.txt") as template:
#     script = (
#         template.read()
#         .format(displacement_x=displacement_x, displacement_y=displacement_y)
#         .split("\n")
#     )


# cubit.init([""])
# fc = FidesysComponent()
# fc.start_up_no_args()

# for command in script:
#     cubit.cmd(command)
# fc.writeFC(r"C:\Projects\effective_yield_surface\test.fc", True)
# subprocess.call(
#     [
#         FIDESYS_CALC,
#         r"--input=C:\Projects\effective_yield_surface\test.fc",
#         r"--output=C:\Projects\effective_yield_surface\test.pvd",
#     ]
# )
# cubit.destroy()
subprocess.call(
    [
        PVPYTHON,
        "postprocess.py"
    ]
)