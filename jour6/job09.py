L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

valeur_max = L[0]
valeur_min = L[0]


for x in L:
    
    if x > valeur_max:
        valeur_max = x

    if x < valeur_min:
        valeur_min = x


print("La valeur max est :" , valeur_max)  
print("La valeur min est :" , valeur_min)

