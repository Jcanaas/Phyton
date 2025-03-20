lsita = []
lsita.append(input("introdueix un valor per la llista"))
lsita.append(input("introdueix un valor per la llista"))
lsita.append(input("introdueix un valor per la llista"))
lsita.append(input("introdueix un valor per la llista"))
print(lsita)
valor = (input("introdueix un valor de la llista"))
if lsita(1) == valor:
    print("el valor es troba a la primera posicio")
elif lsita(2) == valor:
    print("el valor es troba a la segona posicio")
elif lsita(3) == valor:
    print("el valor es troba a la tercera posicio")
elif lsita(4) == valor:
    print("el valor es troba a la quarta posicio")
else:
    print("el valor no es troba en la llista")