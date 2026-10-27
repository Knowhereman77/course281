"""Activity 2 10/6/2026 Theo Buckridge
Create multiple plots in one figure.
"""

import numpy as np
from numpy import cos,sin,sqrt
import matplotlib.pyplot as plt

xs = np.linspace(-5,5,300)

plt.subplot(321)
plt.plot(xs,cos(xs))

plt.subplot(322)
plt.plot(xs,sin(xs))

plt.subplot(323)
plt.plot(xs,cos(xs**2))

plt.subplot(324)
plt.plot(xs,sin(xs**2))

plt.subplot(325)
plt.plot(xs,sqrt(cos(xs)))

plt.subplot(326)
plt.plot(xs,sqrt(sin(xs)))

plt.tight_layout()

plt.show()