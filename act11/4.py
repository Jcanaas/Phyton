# Escriu un programa que calcula la suma dels números parells i els números senars dels números entre 1 i 100. Aquest exercici s’ha de fer amb el bucle while.
suma = 0
while suma < 100:
    n = int(input("Introdueix un número: "))
    if n % 2 == 0:
        suma = suma + n
print("La suma dels números parells és:", suma)

suma_senars = 0
while suma_senars < 100:
    n = int(input("Introdueix un número: "))
    if n % 2 != 0:
        suma_senars = suma_senars + n
# print("La suma dels números senars és:", suma_senars)