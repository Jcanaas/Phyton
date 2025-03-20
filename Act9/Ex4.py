lista =["sistemas", "hardware", "ofimatica", "redes"]
notas = []
notas.append(input("Introdueix nota sistemas "))
notas.append(input("Introdueix nota hardware "))
notas.append(input("Introdueix nota ofimatica "))
notas.append(input("Introdueix nota redes"))

if notas[0] < 5:
    print("Sistemas esta suspendido")
   
if notas[1] < 5:
    print("Hardware esta suspendido")
    
if notas[2] < 5:
    print("Ofimatica esta suspendida")
    
if notas[3] < 5:
    print("Redes esta suspendida")
    