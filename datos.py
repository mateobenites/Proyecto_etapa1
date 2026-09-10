# Tuplas para datos fijos 
estados_equipos = ("Disponible", "Asignado", "En reparacion", "Fuera de servicio")
departamentos = ("Administración", "Ventas", "Sistemas", "Marketing")
tipos_equipos = ("Desktop", "Notebook", "Monitor", "Celular")

# Listas paralelas - Estructuca para empleados.
empleados_legajos = []
empleados_nombres = []
empleados_departamentos = []

# Listas paralelas - Estructura para equipos. 
equipos_codigos = []
equipos_tipos  = []
equipos_estados = []
equipos_legajos = []

# Matriz - Departamentos x Tipos, inicializada en 0
matriz_asignaciones = []
for i in departamentos:          # por cada departamento (4 veces)
    fila = []
    for j in tipos_equipos:        # por cada tipo de equipo (4 veces)
        fila.append(0)
    matriz_asignaciones.append(fila)




