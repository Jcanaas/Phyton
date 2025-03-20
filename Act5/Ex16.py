nom1 = input("Digues el nom de 2 llenguatges de programació")
nom2 = input("Digues el nom de 2 llenguatges de programació")
lletra = input("Digues una lletra")
numero = input("Digues un nombre")
mida1 = len(nom1) < numero
mida2 = len(nom2) < numero
comenza1 = nom1[0] == lletra
comenza2 = nom2[0] == lletra
mida = mida1 or mida2
comenza = comenza1 or comenza2
print("Algun valor comenza per la lletra que has dit")
print(comenza)
print("Algun valor te la longitut que has dit")
print(mida)