paisos = ["Espanya", "França", "Alemanya", "Itàlia", "Portugal"]
print(paisos)

num = int(input("escull un numero dins del rang de posicions vàlides"))
if num >= 0:
    print("vols mostrar una porció de la llista que vagi de l'inici de la llista? (si no , fara de la posicio al final)")
    sino = input("si/no")
    if sino == "si":
        print(paisos[0:num])
    else: print(paisos[num:])
else: print("EL valor no es valid")