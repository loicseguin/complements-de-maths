import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2, 4)
ax = plt.figure().add_subplot(111)
ax.plot(x, 2*x**2 - 3*x -1)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_xlabel('$x$', fontsize=16, position=(1.05, 0.1))
ax.set_ylabel('$f(x)$', fontsize=16, position=(0.45, 1.05), rotation=0)
ax.annotate('', xy=(-0.01,20), xytext=(0,15),
            textcoords='offset points', ha='center',
            arrowprops=dict(arrowstyle='<|-', shrinkA=0, shrinkB=0,
                           facecolor='black', linewidth=0.5))
ax.annotate('', xy=(4, 0.03), xytext=(15,0),
            textcoords='offset points', ha='center',
            arrowprops=dict(arrowstyle='<|-', shrinkA=0, shrinkB=0,
                           facecolor='black', linewidth=0.5))
plt.show()