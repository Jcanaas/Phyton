nota_parcial1 = float(input("Introdueix la nota del primer parcial: "))
nota_parcial2 = float(input("Introdueix la nota del segon parcial: "))
nota_practiques = float(input("Introdueix la nota de les pràctiques: "))

if nota_practiques < 4:
    print("Nota final: Suspès (la nota de les pràctiques és inferior a 4)")
else:
    percentatge_parcial1 = float(input("Introdueix el percentatge del primer parcial: "))
    percentatge_parcial2 = float(input("Introdueix el percentatge del segon parcial: "))
    percentatge_practiques = float(input("Introdueix el percentatge de les pràctiques: "))

    if percentatge_parcial1 + percentatge_parcial2 + percentatge_practiques != 100:
        print("Error: Els percentatges no sumen 100%.")
    else:
        nota_final = (nota_parcial1 * percentatge_parcial1 / 100 +
                      nota_parcial2 * percentatge_parcial2 / 100 +
                      nota_practiques * percentatge_practiques / 100)
        if nota_final < 5:
            resultat = "Suspès"
        elif nota_final < 7:
            resultat = "Aprovat"
        elif nota_final < 9:
            resultat = "Notable"
        else:
            resultat = "Excel·lent"
        print(f"Nota final: {nota_final:.2f} ({resultat})")