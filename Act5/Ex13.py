#Demana a l’usuari el nom de 3 professors que et facin classe aquest curs. Guarda els valors a tres variables diferents. Comprova si els 3 noms tenen la mateixa mida i mostra el resultat per pantalla. La frase que es veurà per pantalla ha de ser una frase que tingui sentit
nom1 = input("nom de preofesor")
nom2 = input("nom de preofesor")
nom3 = input("nom de preofesor")
mateixalong = len(nom1) == len(nom2) == len(nom3)
print ("Son de la meteix longitut?")