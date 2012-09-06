=============
Factorisation
=============

La plupart des problèmes qui font intervenir des polynômes peuvent être résolus
en factorisant les polynômes impliqués. Voici quelques méthodes pour factoriser
des polynômes.


Mise en évidence
================

On a vu que l'addition et la multiplication de nombres réels possèdent une
propriété importante, la **distributivité** : :math:`a (b + c) = ab + ac`. Si
on lit cette équation à l'envers, on obtient que :math:`ab + ac = a (b + c)`.
Cette relation est ce qu'on appelle une **mise en évidence**.

Par exemple, on peut factoriser :math:`3u^3 - 9u^2 + 12\pi u` en remarquant que
chaque terme contient un facteur de :math:`3u`

.. math::
    3u^3 - 9u^2 + 12\pi u = 3u (u^2 - 3u + 4\pi)


Mise en évidence double
=======================

Cette méthode s'applique à une expression algébrique contenant quatre termes.
Il se peut que les quatres termes ne possèdent pas un facteur commun, mais que
pris deux à deux, ils en contiennent un. En général, on pourra appliquer la
méthode de mise en évidence double avec des expressions de la forme :math:`ac +
ad + bc + bd`. Il suffit de mettre en évidence un facteur de :math:`a` pour les
deux premiers termes et un facteur de :math:`b` pour les deux derniers.

.. math::
    ac + ad + bc + bd = a(c+d) + b(c+d)

On s'aperçoit alors que les deux termes obtenus on un facteur :math:`c+d` en
commun. En mettant ce facteur commun en évidence on obtient:

.. math::
    ac + ad + bc + bd = (a+b)(c+d)


