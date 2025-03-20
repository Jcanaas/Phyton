# Escriu un programa que llegeixi un número sencer positiu, calcula el factorial (N!) i el mostra per pantalla.
num = int(input("Introdueix un número: "))

if num < 0:
    print("El número ha de ser positiu.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("El factorial de", num, "és", factorial)
