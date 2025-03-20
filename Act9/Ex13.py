# Demanar a l'usuari una llista de 5 paraules
paraules = [
    input("Introdueix la paraula 1: "),
    input("Introdueix la paraula 2: "),
    input("Introdueix la paraula 3: "),
    input("Introdueix la paraula 4: "),
    input("Introdueix la paraula 5: ")]
print("Llista original:", paraules)
paraules_unicas = list(set(paraules))
print("Llista sense paraules repetides:", paraules_unicas)