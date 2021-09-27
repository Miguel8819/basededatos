asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []
for asignatura in asignaturas:
    nota = float(input("¿Qué nota has sacado en " + asignatura + "?"))
    if nota >= 5:
        passed.append(asignatura)
for asignatura in passed:
    asignaturas.remove(asignatura)
print("Tienes que repetir " + str(asignaturas))