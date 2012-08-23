=================
Les nombres réels
=================


Ensembles de nombres
====================

Nombres naturels
    :math:`\mathbb{N} = \{1, 2, 3, \ldots\}`

    Les nombres naturels sont ceux qu'on utilise pour compter. Noter que dans
    notre cours, l'ensemble des nombres naturels n'inclut *pas* le zéro.

Nombres entiers
    :math:`\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots \}`

    Les nombres entiers comprennent tous les nombres naturels, le zéro et tout
    les nombres négatifs.

Nombres rationnels
    :math:`\mathbb{Q} = \left\{\frac{a}{b} \left|\right. \, a \in \mathbb{Z}, b \in \mathbb{Z} \setminus \{ 0 \} \right\}`

    Les nombres rationnels inclut les nombres entiers et toutes les fractions.
    Il est important de noter qu'une fraction ne peut avoir un dénominateur
    nul.

Nombres réels
    :math:`\mathbb{R} = \left\{a,b_1 b_2 b_3 \ldots | \, a \in \mathbb{Z}, b_i \in \mathbb{N} \cup \{0\} \right\}`

    Dans notre cours, les nombres réels sont définis comme les nombres qui
    admettent un développement décimal. Les nombres réels inclut les nombres
    rationnels et les nombres dit irrationnels, c'est-à-dire les nombres dont
    le développement décimal est infini et apériodique (par exemple,
    :math:`\pi` et :math:`\sqrt{2}`).


Opérations sur les nombres réels
================================

Addition
    L'addition de nombres réels possède cinq propriétés fondamentales.
    Pour tout :math:`a, b, c \in \mathbb{R}`,

    #. **Fermeture**: :math:`a + b \in \mathbb{R}`
    #. **Associativité**: :math:`(a + b) + c = a + (b + c)`
    #. **Commutativité**: :math:`a + b = b + a`
    #. **Élément neutre**: :math:`a + 0 = 0 + a = a`  
    #. **Élément opposé**: :math:`a + (-a) = (-a) + a = 0` 

Soustraction
    La soustraction de deux nombres réels est définie comme l'addition de
    l'élément opposé: :math:`a - b = a + (-b)`. Ceci est équivalent à dire que
    :math:`a - b = c` si et seulement si :math:`a = b + c`.

Multiplication
    La multiplication de nombres réels possède cinq propriétés fondamentales.
    Pour tout :math:`a, b, c \in \mathbb{R}`,

    #. **Fermeture**: :math:`a \cdot b \in \mathbb{R}`
    #. **Associativité**: :math:`(a \cdot b) \cdot c = a \cdot (b \cdot c)`
    #. **Commutativité**: :math:`a \cdot b = b \cdot a`
    #. **Élément neutre**: :math:`a \cdot 1 = 1 \cdot a = a`  
    #. **Élément inverse**: :math:`a \cdot \frac{1}{a} = \frac{1}{a} \cdot a = 1` 

    On note que la multiplication est une façon compacte de répéter une
    addition. Par exemple, plutôt que d'écrire :math:`2 + 2 + 2 + 2`, on
    utilise la multiplication :math:`2 \cdot 4`.

Division
    La division est définie comme la multiplication par l'inverse: :math:`a
    \div b = a \cdot \frac{1}{b}`. Ceci est équivalent à dire que
    :math:`\frac{a}{b} = c` si et seulement si :math:`a = b \cdot c`.

Au dix propriétés ci-dessus s'ajoute une propriété qui concerne la combinaison
de l'addition avec la multiplication : la **distributivité**.

.. math::

    a \cdot (b + c) = a \cdot b + a \cdot c


Relation d'ordre
================

Il existe une relation d'ordre entre les nombres réels, c'est-à-dire qu'il est
possible de classer les nombres réels dans un ordre précis. Pour toute paire
:math:`x`, :math:`y` de nombres réels, une, et une seule des trois relations
suivantes est vraie :

    - :math:`x < y` (:math:`x` est plus petit que :math:`y`)
    - :math:`x > y` (:math:`x` est plus grand que :math:`y`)
    - :math:`x = y` (:math:`x` est égal à :math:`y`)


Valeur absolue
==============

La **valeur absolue** d'un nombre réel :math:`x` est définie comme

.. math::
    |x| = \begin{cases}
            x & \text{ si } x \geq 0 \\
            -x & \text{ si } x < 0
          \end{cases}

Par exemple, :math:`|5,349| = 5,349` car :math:`5.349` est plus grand que zéro.
On a aussi :math:`|-3\pi| = -(-3\pi) = 3\pi` car :math:`-3\pi` est inférieur à
zéro.


Distance
========

La distance entre deux nombres réels :math:`a` et :math:`b` est la longueur du
segment de droite reliant ces deux nombres sur la droite réelle. Si :math:`a
\geq b` alors :math:`d(a, b) = a - b`, si :math:`a < b` alors :math:`d(a, b) =
b - a`. On peut écrire cette définition de façon plus compacte en utilisant la
valeur absolue :

.. math::
    d(a, b) = | a - b |

Il est important de se rappeler que la distance entre deux nombres est, par
définition, positive ou nulle.


Puissances
==========

On a vu que la multiplication correspond, pour les nombres entiers, à une addition
répétée. De façon similaire, les **puissances** sont définies comme des
multiplications répétées. Par exemple, plutôt que d'écrire :math:`8\cdot 8
\cdot 8 \cdot 8`, on peut écrire :math:`8^4`.

Ainsi, si :math:`n` est un nombre naturel, on définit, pour tout :math:`x \in
\mathbb{R}`, la :math:`n`-ième puissance de :math:`x` par

.. math::
    x^n = x \cdot x \cdot \ldots \cdot x

où :math:`x` est répété :math:`n` fois. À partir de cette définition, on peut
démontrer les propriétés suivantes :

    Pour tout :math:`x \in \mathbb{R}`, :math:`n, m \in \mathbb{N}`

    #. :math:`x^n \cdot x^m = x^{n+m}`
    #. :math:`\left( x^n \right)^m = x^{nm}`

Pour définir les puissances pour tous les exposants entiers, on fait
l'observation suivante. Pour obtenir :math:`x^2` à partir de :math:`x^1`, il
suffit de multiplier :math:`x^1` par :math:`x`. De même, pour obtenir
:math:`x^3` à partir de :math:`x^2`, il suffit de multiplier par :math:`x`. En
continuant ainsi, on définit toutes les puissances naturelles. Le processus
fonctionne aussi à l'inverse. Par exemple, pour obtenir :math:`x^2` à partir de
:math:`x^3`, il suffit de diviser :math:`x^3` par :math:`x`. Pour obtenir
:math:`x^1` à partir de :math:`x^2`, il suffit de diviser :math:`x^2` par
:math:`x`. En continuant ainsi, on peut définir :math:`x^0` comme :math:`x^1`
divisé par :math:`x`, i.e.: :math:`x^0 = 1`. Ceci fonctionne pour tout :math:`x
\in \mathbb{R}\setminus\{0\}` car on ne peut pas diviser par zéro.

De même, :math:`x^{-1} = x^0 / x = 1/x`. Donc :math:`x` à la puissance
:math:`-1` est l'inverse multiplicatif de :math:`x`. En général, :math:`x^{-n}
= 1/x^{n}`. Les deux propriétés ci-dessus sont encore valides pour les exposants
entiers.

Pour définir les exposant rationnels, on suppose que les deux propriétés
ci-dessus sont valides et on définit :math:`x^{1/n}` comme le nombre réel
(positif, si :math:`n` est pair) qui,
lorsqu'on l'élève à la :math:`n`-ième puissance, donne :math:`x`. Par exemple,
:math:`8^{1/3}` est le nombre réel qui, lorsqu'on l'élève à la troisième
puissance donne :math:`8`. Évidemment, ce nombre est :math:`8^{1/3} = 2`.
Si :math:`x` est négatif, :math:`x^{1/n}` n'est défini que pour :math:`n`
impair.

De façon générale, :math:`x^{a/b} = \left( x^{1/b} \right)^a`.

Il est fréquent de faire référence à :math:`x^{1/n}` comme la **n-ième racine
principale** de :math:`x`, notée :math:`\sqrt[n]{x}`. L'exemple le plus commun
est la **racine carrée**
qui correspond à la **deuxième racine principale**. On note que par définition,
la racine carrée d'un nombre est toujours positive.

.. warning::

    Soit :math:`x \in \mathbb{R}`. Alors :math:`\sqrt{x^2} = | x|`. Pourquoi ?
    Il suffit de considérer le cas où :math:`x` est négatif. Par exemple, si
    :math:`x = -2`, alors :math:`x^2 = 4` et :math:`\sqrt{x^2} = \sqrt{4} = 2
    \ne x`.

Définir rigoureusement les puissances réelles en général demande beaucoup plus
de travail. Ici, on se contentera de supposer qu'il est possible d'élever un
nombre positif à n'importe quelle puissance réelle. Par exemple, :math:`5^\pi
\approx 156,99`.
