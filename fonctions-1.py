import matplotlib.pyplot as plt
import numpy as np
z = np.linspace(-1, 5)
ax = plt.figure().add_subplot(111)
ax.plot(z, -0.5 * z + 3)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_smart_bounds(True)
ax.yaxis.set_ticks([i * 0.5 for i in range(1, 8)])
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_ylim([0,3.5])
ax.set_xlabel('$z$', fontsize=16)
ax.set_ylabel('$h(z)$', fontsize=16)
plt.show()