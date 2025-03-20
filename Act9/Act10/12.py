# Escriu un programa que tingui una llista formada per 10 números. El programa ha de buscar el número a la llista i mostrar a quina posició es troba. Si el número està repetit, només haurà de buscar la primera posició.
llista = []
for i in range(10):
    num = int(input("Introdueix un número: "))
    llista.append(num)
for i in range(10):
    if llista[i] == num:
        print("El número", num, "es troba a la posició", i+1)
