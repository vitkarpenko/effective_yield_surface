import subprocess
from math import cos, radians, sin, sqrt

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Ellipse

from config import PVPYTHON
from utils import cleanup

cleanup(start=True)

for dx in np.linspace(-1, 1, 10):
    for dy in np.linspace(-1, 1, 10):
        displacement_x = 0.1 * dx
        displacement_y = 0.1 * dy
        subprocess.call(
            [
                PVPYTHON,
                r"C:\Projects\effective_yield_surface\calc.py",
                str(displacement_x),
                str(displacement_y),
            ]
        )
        subprocess.call([PVPYTHON, r"C:\Projects\effective_yield_surface\postprocess.py"])

# for phi in range(45, 45 + 180 + 1, 5):
#     displacement_x = 0.1 * cos(radians(phi))
#     displacement_y = 0.1 * sin(radians(phi))
#     subprocess.call(
#         [
#             PVPYTHON,
#             r"C:\Projects\effective_yield_surface\calc.py",
#             str(displacement_x),
#             str(displacement_y),
#         ]
#     )
#     subprocess.call([PVPYTHON, r"C:\Projects\effective_yield_surface\postprocess.py"])


dots_x = []
dots_y = []
with open("outs.csv", "r") as outs:
    for line in outs:
        splitted = line.strip().split(",")
        x, y = map(float, splitted)
        dots_x.append(x)
        dots_y.append(y)


fig = plt.figure(0)
ax = fig.add_subplot(111, aspect="equal")
ell = Ellipse(
    (0, 0),
    width=sqrt(2) * 2,
    height=sqrt(2) * 1.15,
    # height=sqrt(2),
    angle=45,
    fill=None,
    linestyle="--",
)
ax.add_artist(ell)
ax.legend(
    [ell],
    ["Аналитическая кривая текучести (Мизес)"],
    loc=2,
    fontsize=12,
)
ax.plot(dots_x, dots_y, "o")
ax.axhline(y=0, color="#444444")
ax.axvline(x=0, color="#444444")
ax.set_xlabel("$\sigma_{1}/\sigma_{yield}$", fontsize=12)
ax.set_ylabel("$\sigma_{2}/\sigma_{yield}$", fontsize=12)
plt.show()

cleanup()
