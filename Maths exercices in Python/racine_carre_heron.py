# Pour calculer une approximation de la racine carré d'un nombre x, une facon de faire est de calculer
# les termes de la suite définie par Un+1 = 1/2(Un+(x/Un)) et Uo = 1.
# Cette suite se rapproche très rapidement de la valeur racine_carre(x) = U(5)
# Le but de cet exercice est de créer une fonction racine qui prend en entrée x et affiche la valeur de U(5).

# Ma fonction
# Créez ci dessous votre fonction racine(x):

def racine(x):
    return float(u(5, x))


def u(n, x):
    if n == 0:
        return 1
    else:
        return 1 / 2 * (u(n - 1, x) + (x / u(n - 1, x)))

# La méthode la plus simple
def racine(x):
    def u(n):
        if n == 0:
            return 1
        else:
            return (u(n - 1) + x / u(n - 1)) / 2

    return u(5)