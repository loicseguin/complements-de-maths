import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 1000)
ax = plt.figure().add_subplot(111)
ax.plot(x, np.sin(x), x, np.cos(x), x, np.exp(x), x, x**2, x, x, x, np.log(x),
x, np.sqrt(x), linewidth=10, alpha=0.4)
ax.text(1,3.5, '$e^x$', fontsize=16, color='red', alpha=0.5)
ax.text(2,3.5, '$x^2$', fontsize=16, color='cyan', alpha=0.5)
ax.text(3.5,3, '$x$', fontsize=16, color='purple', alpha=0.5)
ax.text(4,1.6, '$\log(x)$', fontsize=16, color='#ffcc00', alpha=0.5)
ax.text(4.4,0.3, '$\cos(x)$', fontsize=16, color='green', alpha=0.5)
ax.text(3.2,0.3, '$\sin(x)$', fontsize=16, color='blue', alpha=0.5)
ax.text(3.7, 2.2, '$\sqrt{x}$', fontsize=16, color='black', alpha=0.5)
ax.set_ylim([-1.5, 4])
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
plt.tight_layout()
plt.show()