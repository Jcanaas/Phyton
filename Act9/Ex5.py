lista = []
lista.append(input("Introdueix un numero "))
lista.append(input("Introdueix un numero "))
lista.append(input("Introdueix un nombre "))

if lista[0] == lista[1] or lista[0] == lista[2]:
    print("Error, alguns valors estan repetits")
elif lista[1] == lista[0] or lista[1] == lista[2]:
    print("Error, alguns valors estan repetits")
elif lista[2] == lista[0] or lista[2] == lista[1]:
    print("Error, alguns valors estan repetits")
else:
    print("Ningun numero esta repetir")