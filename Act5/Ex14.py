nom1 = input("Nom de una beguda")
nom2= input("Nom de una beguda")
nom3 = input("Nom de una beguda")
nom1long = len(nom1) > 7
nom2long = len(nom2) > 7
nom3long = len(nom3) > 7
mesde7 = nom1long or nom2long or nom2long
print("Algun del noms te mes de 7 lletres ?", mesde7 )