estil1 = input("Digues el nom de un genere musical que t'agradi")
estil2 = input("Digues el nom de un genere musical que t'agradi")
lletra = input("Digues una lletra")
numero = input("Digues un numero")
mida1 = len(estil1) < numero
mida2 = len(estil2) < numero
comenza1 = estil1[-1] == lletra
comenza2 = estil2[-1] == lletra
mida = mida1 and mida2
comenza = comenza1 and comenza2
print("Algun valor comenza per la lletra que has dit")
print(comenza)
print("Algun valor te la longitut que has dit")
print(mida)