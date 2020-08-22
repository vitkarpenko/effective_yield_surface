import subprocess
from math import cos, radians, sin

import matplotlib.pyplot as plt
import seaborn as sns

from config import PVPYTHON
from utils import cleanup

sns.set(style="ticks")
sns.palplot(sns.cubehelix_palette(8, start=0.5, rot=-0.75))

cleanup(start=True)

for phi in range(0, 361, 20):
    displacement_x = 0.05 * cos(radians(phi))
    displacement_y = 0.05 * sin(radians(phi))

    subprocess.call(
        [
            PVPYTHON,
            r"C:\Projects\effective_yield_surface\calc.py",
            str(displacement_x),
            str(displacement_y),
        ]
    )
    subprocess.call([PVPYTHON, r"C:\Projects\effective_yield_surface\postprocess.py"])

dots_x = []
dots_y = []
with open("outs.csv", "r") as outs:
    for line in outs:
        splitted = line.strip().split(",")
        x, y = float(splitted[0]), float(splitted[1])
        dots_x.append(x)
        dots_y.append(y)

plt.plot(dots_x, dots_y, "bo")
plt.show()

cleanup()
