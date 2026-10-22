def my_long_word(nombre, phrase):
    mots = phrase.split()
    resultat = []

    for mot in mots:
        longueur = 0

        for lettre in mot:
            longueur = longueur + 1

        if longueur > nombre:
            resultat.append(mot)

    return " ".join(resultat)


print(my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"))