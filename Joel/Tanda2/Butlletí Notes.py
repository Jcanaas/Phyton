#Un Institut amb mètodes d'educació moderns va intentar fer que els alumnes es posessin les notes del butlletí ells mateixos. No va funcionar.

#Entrada
#Cada cas és d'una línea, i conté un número enter, N
#, del 0 al 10.

#Sortida
#Per cada cas es dira el següent:

#0-4: "Suspes"
#5-6: "Aprovat"
#7-8: "Notable"
#9-10: "Excelent"
#(Excel·lent du punt volat però és molt mala idea posar caràcters especials en els casos de prova...)

nota = int(input())

if nota >= 0 and nota <= 4:
    print("Suspes")
elif nota >= 5 and nota <= 6:
    print("Aprovat")
elif nota >= 7 and nota <= 8:
    print("Notable")
elif nota >= 9 and nota <= 10:
    print("Excelent")
