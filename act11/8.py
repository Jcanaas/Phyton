# Escriu un programa que llegeixi una seqüència de 10 números per teclat i en acabar mostra per pantalla el més gran, el més petit i la mitjana aritmètica de tots ells. Aquest exercici s’ha de fer amb el bucle while.
lista = []
i = 0

while i < 10:
    num = int(input("Introdueix el número", i+1 ))
    lista.append(num)
    i += 1

max_num = max(lista)
min_num = min(lista)
mitjana = sum(lista) / len(lista)

print("El número més gran és:", max_num)
print("El número més petit és:", min_num)
print("La mitjana aritmètica és:", mitjana)