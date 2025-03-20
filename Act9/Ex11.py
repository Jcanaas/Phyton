# Crea un programa que demani una llista de 5 paraules a l’usuari. Mostra la llista per pantalla. A continuació, el programa ha de demanar dues paraules més. Ha de substituir la primera paraula per la segona a la llista.
paraules = []
paraules.append(input("Introdueix una paraula "))
paraules.append(input("Introdueix una paraula "))
paraules.append(input("Introdueix una paraula "))
paraules.append(input("Introdueix una paraula "))
paraules.append(input("Introdueix una paraula "))
print(paraules)

paraula1 = input("Introdueix una paraula ")
paraula2 = input("Introdueix una paraula ")

find1 = paraules.index(paraula1)
print(find1)
paraules.remplace[find1]