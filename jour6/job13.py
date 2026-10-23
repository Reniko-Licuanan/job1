L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

nouvelle_liste = []

for nombre in L:
    if nombre not in nouvelle_liste:
        nouvelle_liste.append(nombre)

print(nouvelle_liste)
