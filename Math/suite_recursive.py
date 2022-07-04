# Considérons la suite définie par Un+1 = 2Un + 3 avec Uo=2
# Créer une fonction u qui donne la valeur Un pour n donné.
# Entrée : Un entier n
# Sortie : Une fonction récursive u qui renvoie (avec return) la valeur Un

def u(n):
    if n==0: return 2
    else: return 2*u(n-1)+3

# Ma fonction
def u(n):
    suite=[n]
    suite[0]=2

    if n==0:
        return 2
    else:
        for i in range(0,n):
            suite.append("")
            suite[i+1]=2*suite[i]+3
    return suite[n]