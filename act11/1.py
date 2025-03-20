# Escriu un programa que llegeixi 10 números sencers i digui quants d’ells són positius. Aquest exercici s’ha de fer amb el bucle while.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numerospositius = []
i = 0

while i < 10:
    if numeros[i] > 0:
        numerospositius.append(numeros[i])
    i = i + 1
    
print("Números positius:", numerospositius)
print("Quantitat de números positius:", len(numerospositius))