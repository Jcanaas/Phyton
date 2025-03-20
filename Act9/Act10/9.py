# Escriu un programa que demani a l’usuari un número. A continuació, el programa ha de demanar a l’usuari el nom de tants Pokemons com el primer número proporcionat. Tots aquests noms s’han de guardar a una llista. Després, ha de mostrar el contingut de la llista per pantalla.
num = int(input("Introdueix un número: "))
pokemons = []
for i in range(0,num,1):
    pokemons.append(input("Introdueix el nom del Pokemon: "))
    print(pokemons)