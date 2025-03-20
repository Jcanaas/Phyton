nom1 = input("Digues un nom de un personatge de Bola de drac")
nom2 = input("Digues un nom de un personatge de Bola de drac")
nom3 = input("Digues un nom de un personatge de Bola de drac")
comprovacio1 = nom1[0] == "a"
comprovacio2 = nom2[0] == "a"
comprovacio3 = nom3[0] == "a"
comprovacio = comprovacio1 or comprovacio2 or comprovacio3
print("Aglguns dels personatjes comenza amb A?")
print(comprovacio)