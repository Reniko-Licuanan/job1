montant_initial = 1000
taux_annuel = 2
print("montant intitial : ",montant_initial)
print("taux de rendenment annuel :",taux_annuel)

gain_annuel = montant_initial * ( taux_annuel / 100 )

print("gain est annuel :", gain_annuel)

montant_apres_gain = montant_initial + gain_annuel
print("montant apres gain :", montant_apres_gain)

nouveau_montant = montant_apres_gain + 5000
nouveau_taux = taux_annuel + 2
print("nouveau montant :", nouveau_montant)
print("nouveau taux est :", nouveau_taux)

gain2 = nouveau_montant * ( nouveau_taux / 100)
print("nouveau gain annuel est : ", gain2)

gain_total = gain_annuel + gain2 
print("gain total est :",gain_total)

montant_total = nouveau_montant + gain_total
print("montant total est :" , montant_total)

montant_apres_retrait = montant_total - (montant_total * 10 / 100)
print ("montant après retrait est :", montant_apres_retrait)

gain_officiel = montant_apres_retrait * (3 / 100)
print("gain officiel est :", gain_officiel)

montant_final = montant_apres_retrait + gain_officiel 
print("montant final est :" , montant_final )




