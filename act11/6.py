# Escriu un programa que llegeixi una seqüència de números sencers fins a llegir un zero. Després ha de mostrar per pantalla quin és el número més gran que s’ha introduït.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0] 
max = 0
i = 0

while lista[i] != 0:
    if lista[i] > max:
        max = lista[i]
    i = i + 1

print(max)