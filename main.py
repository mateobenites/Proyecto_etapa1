import operaciones

opcion = ""

while opcion != "10":
    print("\n--- GESTIÓN DE EQUIPAMIENTO ---")
    print("0. Acerca del sistema")
    print("1. Registrar equipo")
    print("2. Registrar empleado")
    print("3. Asignar equipo")
    print("4. Registrar devolución")
    print("5. Modificar estado de equipo")
    print("6. Buscar equipo")
    print("7. Consultar equipos de un empleado")
    print("8. Listar inventario")
    print("9. Estadísticas e informes")
    print("10. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "0":
        print("\n--- ACERCA DEL SISTEMA ---")
        print("Sistema de Administración de Equipamiento Tecnológico.")
        print("Permite registrar equipos y empleados, asignar y devolver")
        print("dispositivos, controlar su estado y consultar estadísticas")
        print("generales del inventario de la organización.")

    elif opcion == "1":
        codigo = input("Ingrese el código del equipo: ").strip().upper()
        tipo = input("Ingrese el tipo: Desktop, Notebook, Monitor o Celular: ").strip().capitalize()

        operaciones.registrar_equipo(codigo, tipo)

    elif opcion == "2":
        legajo = input("Ingrese el número de legajo (1000 a 9999): ").strip()
        nombre = input("Ingrese el nombre y apellido: ").strip()
        departamento = input("Ingrese el departamento: Administración, Ventas, Sistemas o Marketing: ").strip().capitalize()

        if departamento == "Administracion":
            departamento = "Administración"

        operaciones.registrar_empleado(legajo, nombre, departamento)

    elif opcion == "3":
        codigo = input("Ingrese el código del equipo a asignar: ").strip().upper()
        legajo = input("Ingrese el legajo del empleado: ").strip()

        operaciones.asignar_equipo(codigo, legajo)

    elif opcion == "4":
        codigo = input("Ingrese el código del equipo a devolver: ").strip().upper()

        operaciones.devolver_equipo(codigo)

    elif opcion == "5":
        codigo = input("Ingrese el código del equipo: ").strip().upper()
        nuevo_estado = input("Ingrese el nuevo estado: En reparacion, Disponible o Fuera de servicio: ").strip().capitalize()

        operaciones.modificar_estado_equipo(codigo, nuevo_estado)

    elif opcion == "6":
        codigo = input("Código del equipo: ").strip().upper()
        operaciones.buscar_equipo_por_codigo(codigo)

    elif opcion == "7":
        legajo = input("Legajo del empleado: ").strip()
        operaciones.buscar_empleado_por_legajo(legajo)

    elif opcion == "8":
        print("\n--- LISTA DE EQUIPOS ---")
        operaciones.listar_inventario()

    elif opcion == "9":
        print("\n=== ESTADÍSTICAS E INFORMES ===")

        print("\n--- 1. Inventario General ---")
        operaciones.listar_inventario()

        print("\n--- 2. Equipamiento por Departamento ---")
        operaciones.informe_equipamiento_por_departamento()

        print("\n--- 3. Listado por Estados ---")
        operaciones.informe_listado_por_estados()

        print("\n--- 4. Ranking de Departamentos ---")
        operaciones.ranking_departamentos()

        print("\n--- 5. Resumen General del Inventario ---")
        operaciones.informe_resumen_general()

        print("\n--- Totales por Departamento ---")
        operaciones.total_asignados_por_departamento()

        print("\n--- Totales por Tipo de Equipo ---")
        operaciones.total_asignados_por_tipo()

        print("\n--- Equipos en Reparación ---")
        operaciones.contar_en_reparacion()

        print("\n--- Equipos Disponibles (filtro) ---")
        operaciones.filtrar_equipos_disponibles()

        print("\n--- Alertas de Baja Disponibilidad ---")
        operaciones.alerta_baja_disponibilidad()

    elif opcion == "10":
        print("Programa finalizado")

    else:
        print("Opción inválida. Intente nuevamente.")