# Escriu un programa que demani dos números a l’usuari. Seguidament ha de mostrar per pantalla tots els números compresos entre aquests dos. Comprova quin dels dos números és més petit per tenir en compte com muntar el bucle.
num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))
if num1 > num2:
    for i in range(num2, num1+1):
        print(i)
else:
    for i in range(num1, num2+1):
        print(i)