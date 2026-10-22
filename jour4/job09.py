def moyenne( note1, note2, note3):
    return (note1 + note2 + note3) / 3

note1 = float(input("Tape ta 1er note :"))
print()
note2 = float(input("Tape ta 2eme note :  "))
print()
note3 = float(input("Tape ta 3eme note :"))
print()


moyenne_etudiant = moyenne(note1, note2, note3)

print(moyenne_etudiant)

if 15 <= moyenne_etudiant <= 20 :
    print("Très bon élève")

elif 11 <= moyenne_etudiant <= 14 : 
    print("Bon élève")

elif 8 <= moyenne_etudiant <= 10 : 
    print("Élève moyen")

elif 0 <= moyenne_etudiant <= 7 : 
    print("Éleve devant faire des efforts")

