L = [8 , 24, 48, 2, 16]

compteur = 0

for multiple3 in L: 
    if multiple3 % 3 == 0:
        compteur += 1

print("multiple de 3: ",compteur)