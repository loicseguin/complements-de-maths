.. Compléments de mathématiques documentation master file, created by
   sphinx-quickstart on Tue Jul 31 21:20:33 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. plot::
    :height: 400px

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


====================
Description du cours
====================

Dans le cours de *Compléments de mathématiques* vous apprendrez à manipuler des
expressions algébriques, à utiliser des fonctions algébriques et
transcendantes, et à démontrer des résultats mathématiques avec des preuves par
induction.  Ces notions seront indispensables dans les cours de mathématiques
et de sciences plus avancés. On encourage le développement du sens critique, de
la rigueur et de l’esprit d’analyse et de synthèse. Les cours magistraux seront
accompagnés de séances d’exercices au cours desquelles vous mettrez en pratique
les notions apprises en classe.

Horaire
=======

Groupe 301
    - jeudi 15h à 16h50, de Léry A2004
    - vendredi 13h à 14h50, de Léry A1006

Groupe 302
    - lundi 10h à 11h50, de Léry A2002
    - vendredi 8h à 9h50, de Léry D2047


Contenu du site
===============

.. toctree::
    :titlesonly:

    plandecours
    notesdecours
    devoirs
    ressources
