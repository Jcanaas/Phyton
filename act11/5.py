# Escriu un programa que llegeixi una seqüència de 10 números i ens diu quants són positius, quants són negatius i quants són zero. Aquest exercici s’ha de fer amb el bucle while.
numeros = [1, 2, -3, 4, 5, 6, -7, 8, -9, 0]
numerospositius = 0
numerosnegativs = 0
numeroszeros = 0
i = 0
while len(numeros):
    if numeros[i] == 0: 
        numeroszeros = numeroszeros + 1
    elif numeros[i] > 0:
        numerospositius = numerospositius + 1
    elif numeros[i] < 0:
        numerosnegativs = numerosnegativs + 1
    i = i + 1
print(numerospositius)
print(numerosnegativs) 
print(numeroszeros)