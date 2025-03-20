# Escriu un programa que demani dos números a l’usuari. Seguidament ha de mostrar per pantalla tots els números compresos entre aquests dos. Fes les comprovacions necessàries per a que el primer número sigui més petit que el segon.
num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))
for i in range(num1, num2+1):
    print(i)