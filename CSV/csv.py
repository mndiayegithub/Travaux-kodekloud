import csv


def read_csv_file(file, noms, salaires):
# Lire :  "r",
# Écrire (écraser) :  "w",
# Continuer d’écrire :  "a",
# Lire et écrire (écraser) :  "r+"
    with open(file, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader) #Skip the first row or skip the header

        for ligne in reader:
            noms.append(ligne[0])
            salaires.append(int(ligne[1]))


def write_csv_file(file, noms, salaires):
    header = ("nom", "salaire")  # Créer une ligne pour les entêtes.
    with open(file, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(header)

        # Parcourir les titres et description,
        # zip permet d'itérer sur deux listes ou plus à la fois
        for nom, salaire in zip(noms, salaires):
            ligne = (nom, salaire)
            writer.writerow(ligne)

            # Ici, les salaires sont calculés à l'aide de la formule :
            # heure_travaillées

def main():
    noms = []
    heures_travaillees= []
    salaires = []
    file = "input.csv"

    read_csv_file("input.csv", noms, heures_travaillees)

    #salaire = heure_travailleees * 15
    for i in range(len(heures_travaillees)):
        salaires[i] = heures_travaillees[i] * 15

    write_csv_file("output.csv", noms, salaires)


main()