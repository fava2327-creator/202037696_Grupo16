caudal_l_min = 10.0
for ciclo in range(50):
    if caudal_l_min > 25:
        print("VALIDACION: Lote descartado por turbulencia")
        break
    if caudal_l_min < 12:
        print("Ajuste: Abriendo electrovalvula de entrada")
        caudal_l_min += 1.5
    elif 12 <= caudal_l_min <= 18:
        print("Ajuste: Caudal de destilacion en zona optima")
        caudal_l_min += 0.1
    else:
        print("Ajuste: Cerrando compuerta por exceso de flujo")
        caudal_l_min -= 2.0
