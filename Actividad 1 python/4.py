ganador = []
for i in range(6):
    ganador.append(int(input("Introduce un número ganador: ")))
ganador.sort()
print("Los números ganadores son " + str(ganador))
