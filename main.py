import subprocess
from math import cos, sin

from config import PVPYTHON
from utils import cleanup

cleanup()

for phi in range(0, 361, 120):
    displacement_x = 0.05 * cos(phi)
    displacement_y = 0.05 * sin(phi)

    subprocess.call(
        [
            PVPYTHON,
            r"Z:\effective_yield_surface\calc.py",
            str(displacement_x),
            str(displacement_y),
        ]
    )
    subprocess.call([PVPYTHON, r"Z:\effective_yield_surface\postprocess.py"])

cleanup()
