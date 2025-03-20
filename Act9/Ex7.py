lista = []
lista.append(input("Introdueix un numero "))
lista.append(input("Introdueix un numero "))
lista.append(input("Introdueix un nombre "))
print(lista)

if lista[0] % 2 == 0:
    del (lista[0])
print(lista)