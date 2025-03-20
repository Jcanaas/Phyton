# Escriu un programa que demani a l’usuari 10 números enters i digui quants d’ells són positius.
llista = []
for i in range(10):
    num = int(input("Introdueix un número: "))
    llista.append(num)
pos = 0
for i in range(10):
    if llista[i] > 0:
        pos += 1
print("Hi ha", pos, "números positius.")