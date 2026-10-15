# Tuplas para datos fijos 
estados_equipos = ("Disponible", "Asignado", "En reparación", "Fuera de servicio")
departamentos = ("Administración", "Ventas", "Sistemas", "Marketing")
tipos_equipos = ("Desktop", "Notebook", "Monitor", "Celular")


def crear_datos():
    empleados_legajos = []
    empleados_nombres = []
    empleados_departamentos = []

    equipos_codigos = []
    equipos_tipos = []
    equipos_estados = []
    equipos_legajos = []

    matriz_asignaciones = []

    for i in departamentos:
        fila = []
        for j in tipos_equipos:
            fila.append(0)
        matriz_asignaciones.append(fila)

    return (empleados_legajos, empleados_nombres, empleados_departamentos,
            equipos_codigos, equipos_tipos, equipos_estados, equipos_legajos,
            matriz_asignaciones)



