nom = input("Introdueix el nom del treballador: ")
edat = int(input("Introdueix l'edat del treballador: "))
hores_setmanals = float(input("Introdueix les hores setmanals treballades: "))

if hores_setmanals <= 40:
    salari_setmanal = hores_setmanals * 10
else:
    salari_setmanal = 40 * 10 + (hores_setmanals - 40) * 15
salari_mensual = salari_setmanal * 4
salari_anual = salari_mensual * 14

if edat > 50:
    irpf_percentatge = 15
elif edat > 30 and salari_anual > 20000:
    irpf_percentatge = 18
else:
    irpf_percentatge = 20
irpf_mensual = salari_mensual * irpf_percentatge / 100

print(nom, "té un salari mensual de", salari_mensual, "euros al mes i paga un IRPF de", irpf_mensual, "euros.")