# Escriu un programa que demana un número i mostra per pantalla els números imparells des de l’1 fins al número introduït. Aquest exercici s’ha de fer amb el bucle while. 
num = int(input("Introdueix un número: "))
i = 1
while i <= num:
    if i % 2 == 0:
        print(i)
    i = i + 1
