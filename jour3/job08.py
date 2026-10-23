a = float(input("Entrez longeur a :"))
b = float(input("Entrez longeur b :"))
c = float(input("Entrez longeur c :"))

if a + b > c and b + c > a and c + a > b :
    print("C'est possible de construire un triangle")

if a == b and b == c and c == a:
    print("Le triangle est équilatéral")

elif a == b or b == c or c == a:
    print("Le triangle est isocèle")

else:
    print("Le traingle est quelconque")

if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("on ne peut pas construire un triangle")
