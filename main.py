from config import (
    FIDESYS_BASE_FOLDER,
    FIDESYS_CALC,
    FIDESYS_COM_PATH,
    FIDESYS_LIBPATH,
    FIDESYS_PYTHONPATH,
    FIDESYS_VERSION,
)
import os

os.environ["PYTHONPATH"] = (
    ";".join(FIDESYS_BASE_FOLDER + subpath for subpath in FIDESYS_PYTHONPATH)
    + ";"
    + os.environ.get("PYTHONPATH", "")
)

print(os.environ["PYTHONPATH"])

import subprocess
from fidesys import FidesysComponent
import cubit

displacement_x = 0
displacement_y = 0

with open("template_2d.txt") as template:
    script = template.read().format(
        displacement_x=displacement_x, displacement_y=displacement_y
    )


cubit.init([""])
fc = FidesysComponent()
fc.start_up_no_args()
