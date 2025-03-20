# Crea una llista que contingui el nom de 5 equips de futbol que participen al mundial de futbol. Mostra la llista per pantalla. Demana a l’usuari dos números. Comprova que aquests dos números estan dins del rang de posicions vàlides de la llista. Mostra per pantalla la porció de la llista compresa entre els dos números que ha proporcionat l’usuari
equips = ["Barça", "Real Madrid", "Atlètico", "Barcelona", "Juventus"]
print(equips)

num1 = int(input("Escull un número"))
num2 = int(input("Escull un altre número"))
print(len(equips))

if num1 >= 0 and num1 < len(equips) and num2 >= 0 and num2 < len(equips):
    print(equips[num1:num2])
else:
    print("Error")