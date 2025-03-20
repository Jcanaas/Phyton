# Escriu un programa que contingui una llista amb el nom de 3 colors diferents. S’han de mostrar per pantalla aquests 3 colors.
lista = ["vermell", "blau", "groc"]
for colors in range(0,3,1):
    lista.append(input("Introdueix el nom del color: "))
    print(colors)
