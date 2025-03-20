# Escriu un programa que demani a l’usuari el nom de 5 països. Aquests valors s’han de guardar a una llista. S’ha de mostrar per pantalla una frase com la següent:
# M’agradaria visitar <país>
# On heu de substituir <país> per cada un dels països de la llista.

paissos = []
for i in range(0,5,1):
    paissos.append(input("Introdueix el nom del país: "))
    print("M'agradaria visitar", paissos[-1])