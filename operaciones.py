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
    datos.equipos_legajos.append("")

def registrar_empleado(legajo, nombre, departamento):
    if legajo == "" or nombre == "" or departamento == "":
        print("Error: Legajo, nombre y departamento son obligatorios.")
        return

    if not legajo.isdigit():
        print("Error: Legajo debe ser un número.")
        return

    if len(legajo) != 4 or not 1000 <= int(legajo) <= 9999:
        print("Error: Legajo debe tener 4 dígitos y estar entre 1000 y 9999.")
        return

    if legajo in datos.empleados_legajos:
        print("Error: Ya existe un empleado con este legajo.")
        return

    if departamento not in datos.departamentos:
        print("Error: Departamento invalido.")
        return

    datos.empleados_legajos.append(legajo)
    datos.empleados_nombres.append(nombre)
    datos.empleados_departamentos.append(departamento)

    print("Empleado registrado exitosamente.")

def buscar_posicion(lista, valor_buscado):

    for i in range(len(lista)):
        if lista[i] == valor_buscado:
            return i
    return -1



