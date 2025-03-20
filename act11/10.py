# Escriu un programa que demani 10 números sencers més grans a l’anterior. S’han de mostrar els números per pantalla.
num = 0
i = 0
while i == 10:
    num = int(input("Introdueix un número: "))
    if num > 0:
        print(num)
    i = i + 1