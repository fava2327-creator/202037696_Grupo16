
# ============================================================
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
# Curso: Lenguajes Interpretados
# Grupo: 16
# Tarea 2: Control de presión en red de gas natural
# Escenario 2: Dosificación de presión
# Autora: Jakeline Alzate Gómez
# ============================================================


# ------------------------------------------------------------
# PRESENTACIÓN DEL PROGRAMA
# ------------------------------------------------------------

print("=" * 55)
print("       CONTROL DE PRESIÓN EN RED DE GAS NATURAL")
print("                  ESCENARIO 2")
print("=" * 55)
print("Autora: Jakeline Alzate Gómez")
print("Curso: Lenguajes Interpretados")
print("Grupo: 16")
print("=" * 55)
print()


# ------------------------------------------------------------
# INICIALIZACIÓN DE LA SIMULACIÓN
# ------------------------------------------------------------

# Valor inicial de presión para iniciar la simulación
presion = 1.0


# ------------------------------------------------------------
# CONTROL Y DOSIFICACIÓN DE PRESIÓN
# ------------------------------------------------------------

# Máximo de 10 lecturas para evitar sobrecarga del sistema
for lectura in range(10):

    # Mostrar el número de lectura y la presión actual
    print(f"Lectura {lectura + 1} | Presión: {presion:.1f} bar")

    # Evaluar primero la condición crítica de seguridad
    if presion >= 6.0:
        print("CRÍTICO: Ruptura inminente. Abortar.")
        break

    # Presión insuficiente
    elif presion < 2.0:
        print("Acción: Inyectando presión a la red")
        presion += 0.5

    # Presión dentro del rango nominal
    elif presion <= 4.5:
        print("Acción: Flujo nominal estabilizado")
        presion += 0.1
