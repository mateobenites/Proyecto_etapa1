import datos


def buscar_posicion(lista, valor_buscado):
    for i in range(len(lista)):
        if lista[i] == valor_buscado:
            return i
    return -1


def registrar_equipo(codigo, tipo, equipos_codigos, equipos_tipos, equipos_estados, equipos_legajos):
    if codigo == "" or tipo == "":
        print("Error: Codigo o tipo son obligatorios.")
        return

    if not codigo.isalnum():
        print("Error: Codigo debe ser alfanumérico.")
        return

    if codigo in datos.equipos_codigos:
        print("Error: Ya existe un equipo con este codigo.")
        return

    if tipo not in datos.tipos_equipos:
        print("Error: Tipo invalido.")
        return

    equipos_codigos.append(codigo)
    equipos_tipos.append(tipo)
    equipos_estados.append("Disponible")
    equipos_legajos.append("")

    print("Equipo registrado exitosamente.")

def registrar_empleado(legajo, nombre, departamento, empleados_legajos, empleados_nombres, empleados_departamentos):
    if legajo == "" or nombre == "" or departamento == "":
        print("Error: Legajo, nombre y departamento son obligatorios.")
        return

    if not legajo.isdigit():
        print("Error: Legajo debe ser un número.")
        return

    if len(legajo) != 4 or not 1000 <= int(legajo) <= 9999:
        print("Error: Legajo debe tener 4 dígitos y estar entre 1000 y 9999.")
        return

    if legajo in empleados_legajos:
        print("Error: Ya existe un empleado con este legajo.")
        return

    if departamento not in datos.departamentos:
        print("Error: Departamento invalido.")
        return

    empleados_legajos.append(legajo)
    empleados_nombres.append(nombre)
    empleados_departamentos.append(departamento)

    print("Empleado registrado exitosamente.")


def asignar_equipo(codigo, legajo, equipos_codigos, equipos_tipos, equipos_estados, equipos_legajos, empleados_legajos, empleados_departamentos, matriz_asignaciones):
    pos_equipo = buscar_posicion(equipos_codigos, codigo)
    if pos_equipo == -1:
        print("Error: No existe un equipo con este codigo.")
        return

    pos_empleado = buscar_posicion(empleados_legajos, legajo)
    if pos_empleado == -1:
        print("Error: No existe un empleado con este legajo.")
        return

    if equipos_estados[pos_equipo] != "Disponible":
        print("Error: El equipo debe estar Disponible para poder asignarlo.")
        return

    departamento = empleados_departamentos[pos_empleado]
    tipo = equipos_tipos[pos_equipo]

    pos_depto = datos.departamentos.index(departamento)
    pos_tipo = datos.tipos_equipos.index(tipo)

    equipos_estados[pos_equipo] = "Asignado"
    equipos_legajos[pos_equipo] = legajo
    matriz_asignaciones[pos_depto][pos_tipo] += 1

    print("Equipo asignado exitosamente.")

def devolver_equipo(codigo, equipos_codigos, equipos_tipos, equipos_estados, equipos_legajos, empleados_legajos, empleados_departamentos, matriz_asignaciones):
    pos_equipo = buscar_posicion(equipos_codigos, codigo)

    if pos_equipo == -1:
        print("Error: No existe un equipo con este codigo.")
        return

    if equipos_estados[pos_equipo] != "Asignado":
        print("Error: El equipo no esta asignado, no se puede devolver.")
        return

    legajo = equipos_legajos[pos_equipo]

    if legajo == "":
        print("Error: El equipo no tiene un empleado asociado.")
        return

    pos_empleado = buscar_posicion(empleados_legajos, legajo)
    departamento = empleados_departamentos[pos_empleado]
    tipo = equipos_tipos[pos_equipo]

    pos_depto = datos.departamentos.index(departamento)
    pos_tipo = datos.tipos_equipos.index(tipo)

    if matriz_asignaciones[pos_depto][pos_tipo] > 0:
        matriz_asignaciones[pos_depto][pos_tipo] -= 1

    equipos_estados[pos_equipo] = "Disponible"
    equipos_legajos[pos_equipo] = ""

    print("Equipo devuelto exitosamente.")


def modificar_estado_equipo(codigo, nuevo_estado, equipos_codigos, equipos_estados):
    pos_equipo = buscar_posicion(equipos_codigos, codigo)

    if pos_equipo == -1:
        print("Error: No existe un equipo con este codigo.")
        return

    if nuevo_estado not in datos.estados_equipos:
        print("Error: Estado invalido.")
        return

    estado_actual = equipos_estados[pos_equipo]

    if estado_actual == "Asignado":
        print("Error: El equipo esta asignado. Debe devolverlo antes de cambiar su estado.")
        return

    if estado_actual == "Fuera de servicio":
        print("Error: Un equipo Fuera de servicio no puede cambiar de estado.")
        return

    if estado_actual == "Disponible" and nuevo_estado != "En reparación":
        print("Error: Desde Disponible solo se puede pasar a En reparación.")
        return

    if estado_actual == "En reparación" and nuevo_estado not in ("Disponible", "Fuera de servicio"):
        print("Error: Desde En reparación solo se puede pasar a Disponible o Fuera de servicio.")
        return

    equipos_estados[pos_equipo] = nuevo_estado
    print("Estado actualizado exitosamente.")


def buscar_equipo_por_codigo(codigo, equipos_codigos, equipos_tipos, equipos_estados, equipos_legajos, empleados_legajos, empleados_nombres, empleados_departamentos):
    if codigo not in equipos_codigos:
        print("No existe ese equipo.")
        return

    i = equipos_codigos.index(codigo)
    legajo = equipos_legajos[i]

    if legajo in empleados_legajos:
        j = empleados_legajos.index(legajo)
        print(equipos_codigos[i], equipos_tipos[i], equipos_estados[i],
              empleados_nombres[j], empleados_departamentos[j])
    else:
        print(equipos_codigos[i], equipos_tipos[i], equipos_estados[i], "Sin asignar")


def buscar_empleado_por_legajo(legajo, empleados_legajos, empleados_nombres, empleados_departamentos, equipos_codigos, equipos_tipos, equipos_estados, equipos_legajos):
    if legajo not in empleados_legajos:
        print("No existe ese empleado.")
        return

    i = empleados_legajos.index(legajo)

    print("Legajo:", legajo)
    print("Nombre:", empleados_nombres[i])
    print("Departamento:", empleados_departamentos[i])

    for k in range(len(equipos_codigos)):
        if equipos_legajos[k] == legajo:
            print(" -", equipos_codigos[k], equipos_tipos[k], equipos_estados[k])

def listar_inventario(equipos_codigos, equipos_tipos, equipos_estados):
    if len(equipos_codigos) == 0:
        print("Todavía no hay equipos registrados.")
        return

    for i in range(len(equipos_codigos)):
        print(
            f"Codigo: {equipos_codigos[i]} | "
            f"Tipo: {equipos_tipos[i]} | "
            f"Estado: {equipos_estados[i]}"
        )


def total_asignados_por_departamento(matriz_asignaciones):
    for i in range(len(datos.departamentos)):
        print(datos.departamentos[i], ":", sum(matriz_asignaciones[i]))


def total_asignados_por_tipo():
    for j in range(len(datos.tipos_equipos)):
        print(datos.tipos_equipos[j], ":", sum(fila[j] for fila in datos.matriz_asignaciones))


def porcentaje_equipos_asignados():
    if not datos.equipos_estados:
        print("No hay equipos.")
        return
    asignados = datos.equipos_estados.count("Asignado")
    print("Porcentaje asignado:", round(asignados / len(datos.equipos_estados) * 100, 2), "%")


def contar_en_reparacion():
    print("En reparación:", datos.equipos_estados.count("En reparación"))


def departamento_mayor_asignacion():
    totales = [sum(fila) for fila in datos.matriz_asignaciones]
    maximo = max(totales)
    if maximo == 0:
        print("No hay equipos asignados.")
        return
    for i in range(len(datos.departamentos)):
        if totales[i] == maximo:
            print(datos.departamentos[i], ":", maximo)


def alerta_baja_disponibilidad():
    for tipo in datos.tipos_equipos:
        disponibles = sum(1 for i in range(len(datos.equipos_tipos))
                           if datos.equipos_tipos[i] == tipo and datos.equipos_estados[i] == "Disponible")
        if disponibles < 2:
            print("Alerta:", tipo, "-", disponibles, "disponibles")


def ranking_departamentos():
    totales = []
    for i in range(len(datos.departamentos)):
        totales.append((datos.departamentos[i], sum(datos.matriz_asignaciones[i])))

    obtener_cantidad = lambda x: x[1]

    for i in range(len(totales)):
        indice_mayor = i
        for j in range(i + 1, len(totales)):
            if obtener_cantidad(totales[j]) > obtener_cantidad(totales[indice_mayor]):
                indice_mayor = j
        totales[i], totales[indice_mayor] = totales[indice_mayor], totales[i]

    ranking = totales[:3]

    for depto, cantidad in ranking:
        print(depto, ":", cantidad)


def filtrar_equipos_disponibles():
    disponibles = [datos.equipos_codigos[i] for i in range(len(datos.equipos_codigos))
                   if datos.equipos_estados[i] == "Disponible"]
    print(disponibles)


def informe_equipamiento_por_departamento():
    for i in range(len(datos.departamentos)):
        depto = datos.departamentos[i]
        print(f"\n{depto}:")
        hay_equipos = False
        for k in range(len(datos.equipos_codigos)):
            legajo = datos.equipos_legajos[k]
            if legajo != "":
                pos_empleado = buscar_posicion(datos.empleados_legajos, legajo)
                if pos_empleado != -1 and datos.empleados_departamentos[pos_empleado] == depto:
                    hay_equipos = True
                    print(" -", datos.equipos_codigos[k], datos.equipos_tipos[k])
        if not hay_equipos:
            print(" Sin equipos asignados.")
        print("Total asignado:", sum(datos.matriz_asignaciones[i]))


def informe_listado_por_estados():
    for estado in datos.estados_equipos:
        print(f"\n{estado}:")
        encontrados = [datos.equipos_codigos[i] for i in range(len(datos.equipos_codigos))
                       if datos.equipos_estados[i] == estado]
        if encontrados:
            print(encontrados)
        else:
            print("Ninguno.")


def informe_resumen_general():
    total = len(datos.equipos_codigos)
    print("Cantidad total de equipos:", total)

    for estado in datos.estados_equipos:
        cantidad = datos.equipos_estados.count(estado)
        print(f"{estado}: {cantidad}")

    porcentaje_equipos_asignados()
    departamento_mayor_asignacion()