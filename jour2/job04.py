n = int(input("Entrez un entier supérieur à 0 :"))

for table in range(1, n + 1): 
    print("Table de multiplication de", table)

    for multiplicator in range(1, 11):
        resultat = table * multiplicator
        print(table, "x", multiplicator, "=", resultat)
    





    