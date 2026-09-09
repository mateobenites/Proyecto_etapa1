import datos

def registrar_equipo(codigo, tipo):
    if codigo == "" or tipo == "":
        print("Error: Codigo o tipo son obligatorios.")
        return

    if codigo in datos.equipos_codigos:
        print("Error: Ya existe un equipo con este codigo.")
        return

    if tipo not in datos.tipos_equipos:
        print("Error: Tipo invalido.")
        return


    datos.equipos_codigos.append(codigo)
    datos.equipos_tipos.append(tipo)
    datos.equipos_estados.append("Disponible")
    datos.equipos_legajos.append(None)
