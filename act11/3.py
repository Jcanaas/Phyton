# Escriu un programa que llegeix una seqüència de notes senceres (0..10) fins que llegeix el -1 i digui si alguna de les notes era un 10.
notes = [0, 1, 2, 10, 4, 10, 6, 7, 8, 9, 10]
i = len(notes)
y = 0
i10 = False
print(len(notes))
for i in range(len(notes)):
    if notes[y] == 10:
        i10 = True
    y = y + 1
if i10 == True :
    print("Sí, alguna de les notes era un 10.")
