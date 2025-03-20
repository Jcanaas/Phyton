# Escriu un programa que demani un nombre sencer i ens mostri la suma de tots els números des de l’1 fins al número introduït. El resultat de la suma s’ha de mostrar per pantalla.
num = int(input("Introdueix un número: "))
i = 0
while i < num:
    suma = suma + i
    i = i + 1
print(suma)