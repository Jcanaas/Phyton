lista = []
lista.append(input("Introdueix un numero "))
lista.append(input("Introdueix un numero "))
lista.append(input("Introdueix un nombre "))
if lista[0] > lista[1] and lista[0] > lista[2]: print("El primer numero és el més gran")
elif lista[1] > lista[0] and lista[1] > lista[2]: print("El segon numero és el més gran")  
elif lista[2] > lista[0] and lista[2] > lista[1]:print("El tercer numero és el més gran")  
else: print("No hi ha un més gran")