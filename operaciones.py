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


from datos import (departamentos, tipos_equipos,
    empleados_legajos, empleados_nombres, empleados_departamentos,
    equipos_codigos, equipos_tipos, equipos_estados, equipos_legajos,
    matriz_asignaciones)


def buscar_equipo_por_codigo():
    codigo = input("Código del equipo: ")
    if codigo not in equipos_codigos:
        print("No existe ese equipo.")
        return

    i = equipos_codigos.index(codigo)
    legajo = equipos_legajos[i]

    if legajo in empleados_legajos:
        j = empleados_legajos.index(legajo)
        print(equipos_codigos[i], equipos_tipos[i], equipos_estados[i], empleados_nombres[j], empleados_departamentos[j])
    else:
        print(equipos_codigos[i], equipos_tipos[i], equipos_estados[i], "Sin asignar")


def buscar_empleado_por_legajo():
    legajo = int(input("Legajo del empleado: "))
    if legajo not in empleados_legajos:
        print("No existe ese empleado.")
        return

    i = empleados_legajos.index(legajo)
    print(empleados_nombres[i], empleados_departamentos[i])

    for k in range(len(equipos_codigos)):
        if equipos_legajos[k] == legajo:
            print(" -", equipos_codigos[k], equipos_tipos[k], equipos_estados[k])


def total_asignados_por_departamento():
    for i in range(len(departamentos)):
        print(departamentos[i], ":", sum(matriz_asignaciones[i]))


def total_asignados_por_tipo():
    for j in range(len(tipos_equipos)):
        print(tipos_equipos[j], ":", sum(fila[j] for fila in matriz_asignaciones))


def porcentaje_equipos_asignados():
    if not equipos_estados:
        print("No hay equipos.")
        return
    asignados = equipos_estados.count("Asignado")
    print("Porcentaje asignado:", round(asignados / len(equipos_estados) * 100, 2), "%")


def contar_en_reparacion():
    print("En reparación:", equipos_estados.count("En reparacion"))


def departamento_mayor_asignacion():
    totales = [sum(fila) for fila in matriz_asignaciones]
    maximo = max(totales)
    if maximo == 0:
        print("No hay equipos asignados.")
        return
    for i in range(len(departamentos)):
        if totales[i] == maximo:
            print(departamentos[i], ":", maximo)


def alerta_baja_disponibilidad():
    for tipo in tipos_equipos:
        disponibles = sum(1 for i in range(len(equipos_tipos)) if equipos_tipos[i] == tipo and equipos_estados[i] == "Disponible")
        if disponibles < 2:
            print("Alerta:", tipo, "-", disponibles, "disponibles")


def ranking_departamentos():
    totales = [(departamentos[i], sum(matriz_asignaciones[i])) for i in range(len(departamentos))]
    ranking = sorted(totales, key=lambda x: x[1], reverse=True)[:3]
    for depto, cantidad in ranking:
        print(depto, ":", cantidad)


def filtrar_equipos_disponibles():
    disponibles = [equipos_codigos[i] for i in range(len(equipos_codigos)) if equipos_estados[i] == "Disponible"]
    print(disponibles)
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

def asignar_equipo(codigo,legajo):

    posicion_equipo = buscar_posicion(datos.equipos_codigos, codigo)

    if posicion_equipo == -1:
        print("Error: No existe un equipo con este codigo.")
        return

    posicion_empleado = buscar_posicion(datos.empleados_legajos, legajo)

    if posicion_empleado == -1:
        print("Error: No existe un empleado con este legajo.")
        return


