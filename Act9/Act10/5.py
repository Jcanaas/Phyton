# Escriu un programa que demani 3 números a l’usuari. Els dos primers números són per indicar el rang que es mostrarà per pantalla. El tercer és per indicar l’increment per mostrar aquests números. Fes les comprovacions necessàries per que el primer número sigui més petit que el segon i que el tercer estigui a dins del rang. Per exemple, si l’usuari posa 1, 10 i 3, mostrarà el rang del 1 al 9 fent salts de 3 en 3. …
num1 = int(input("Introdueix el primer número (límit inferior): "))
num2 = int(input("Introdueix el segon número (límit superior): "))
num3 = int(input("Introdueix el tercer número (increment): "))

if num1 >= num2:
    print("Error: El primer número ha de ser més petit que el segon.")
elif num3 <= 0 or num3 >= (num2 - num1):
    print("Error: L'increment ha de ser positiu i dins del rang.")
else:
    for i in range(num1, num2, num3):
        print(i)
