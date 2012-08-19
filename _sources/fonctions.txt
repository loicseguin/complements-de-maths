=====================
Les fonctions de base
=====================

Fonctions polynômiales
======================

Une fonction de la forme

.. math::

    f(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_2 x^2 + a_1 x + a_0

est dite polynômiale. Ce type de fonctions comprend les fonctions linéaires,
:math:`f(x) = ax + b` et les fonctions quadratiques :math:`f(x) = ax^2 + bx + c`.

Fonction linéaire
-----------------
Pour une fonction linéaire :math:`g(u) = cu + d`, on appelle :math:`c` la
**pente** et :math:`d` l'**ordonnée à l'origine**. Le graphe d'une fonction
linéaire est une droite. La figure suivante illustre la fonction linéaire
:math:`h(z) = -\frac{2}{3} z + 3`.

.. plot::

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

Cette fonction possède un seul **zéro** : :math:`z = 9/2`.


Fonction quadratique
--------------------
Le graphe d'une fonction quadratique :math:`f(x) = ax^2 + bx + c`, où :math:`a \ne 0`
est une parabole. Si :math:`a > 0`, la parabole est ouverte vers le haut, sinon
elle est ouverte vers le bas. La figure suivante illustre le graphe de la
fonction :math:`f(x) = 2x^2 - 3x - 1`.

.. plot::

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

Cette fonction possède deux zéros : :math:`z = (3 + \sqrt{17}) / 4` et :math:`z
= (3 - \sqrt{17}) / 4`.


Le théorème fondamental de l'algèbre
------------------------------------
*Toute fonction polynômiale de degré* :math:`n` *possède au plus* :math:`n` *zéros,
en comptant les multiplicités.*

En réalité, le théorème fondamental de l'algèbre traite de polynômes définis
sur l'ensemble des nombres complexes et son énoncé n'est pas tout à fait le
même, mais il est équivalent.

Il est intéressant de remarquer que pour les polynômes complexes l'énoncé est
beaucoup plus satisfaisant :

    Toute fonction polynômiale complexe de degré :math:`n` possède *exactement*
    :math:`n` zéros, en comptant les multiplicités.
