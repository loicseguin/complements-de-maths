import matplotlib.pyplot as plt
import numpy as np
z = np.linspace(-1, 5)
ax = plt.figure().add_subplot(111)
ax.plot(z, -0.66666667 * z + 3)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_smart_bounds(True)
ax.yaxis.set_ticks([i * 0.5 for i in range(1, 8)])
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_ylim([0,3.5])
ax.set_xlabel('$z$', fontsize=16, position=(1.05, 0.1))
ax.set_ylabel('$h(z)$', fontsize=16, position=(0.45, 1.05), rotation=0)
ax.annotate('', xy=(1./6.,1), xycoords='axes fraction', xytext=(0,15),
            textcoords='offset points', ha='center',
            arrowprops=dict(arrowstyle='<|-', shrinkA=0, shrinkB=0,
                           facecolor='black', linewidth=0.5))
ax.annotate('', xy=(1,0.001), xycoords='axes fraction', xytext=(15,0),
            textcoords='offset points', ha='center',
            arrowprops=dict(arrowstyle='<|-', shrinkA=0, shrinkB=0,
                           facecolor='black', linewidth=0.5))
plt.show()