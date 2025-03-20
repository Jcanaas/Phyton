# Escriu un programa que tingui una llista formada per 10 números. El programa ha de sumar tots els números de la llista y guardar el resultat a una variable. Després ha de mostrar tot el contingut de la llista i el resultat final de la suma.
llista = []
for i in range(10):
    num = int(input("Introdueix un número: "))
    llista.append(num)
suma = 0
for num in llista:
    suma += num
print("Llista de números:", llista)
print("Suma total:", suma)
