# Escriu un programa que demani a l’usuari el nom de 5 animals. Aquests valors s’han de guardar a una llista. Després, s’han de mostrar els valors per pantalla. 
lista = []
for i in range(0,5,1):
    lista.append(input("Introdueix el nom de l'animal: "))
    print(lista)