mapa_bme680 = { 
    "0x60": {"status": True, "calib_val": 12, "limit": 100}, 
    "0x61": {"status": True, "calib_val": 55, "limit": 200}, 
    "0x62": {"status": False, "calib_val": 88, "limit": 90}, 
} 
 
def consultar_registro(direccion_hex): 
    registro = mapa_bme680.get(direccion_hex) 
    if registro is None: 
        return f"Error: direccion '{direccion_hex}' no encontrada." 
    return registro 
 
if __name__ == "__main__": 
    print(consultar_registro("0x60")) 
    print(consultar_registro("0x91")) 
