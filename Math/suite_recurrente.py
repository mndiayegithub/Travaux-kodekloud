# Soit une suite recurrente définie par Un+1 = 2Un + 3Un-1 avec Uo=2 et U1=1
# Créer une fonction u qui donne la valeur Un avec un n donné.
# Entrée : Un entier n
# Sortie : Une fonction récursive u qui renvoie (avec return) la valeur Un.

def u(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return 2*u(n-1)+3*u(n-2)