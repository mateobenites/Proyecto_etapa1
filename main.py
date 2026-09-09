import datos
import operaciones

opcion = ""

while opcion != "3":
    print("\n--- GESTIÓN DE EQUIPAMIENTO ---")
    print("1. Registrar equipo")
    print("2. Listar equipos")
    print("3. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        codigo = input("Ingrese el código del equipo: ").strip().upper()

        tipo = input("Ingrese el tipo: Desktop, Notebook, Monitor o Celular: ").strip().capitalize()

        operaciones.registrar_equipo(codigo, tipo)

    if opcion == "2":
        print("\n--- LISTA DE EQUIPOS ---")

        if len(datos.equipos_codigos) == 0:
            print("Todavía no hay equipos registrados.")

        else:
            for i in range(len(datos.equipos_codigos)):
                print(
                    f"Codigo: {datos.equipos_codigos[i]}"
                    f"Tipo: {datos.equipos_tipos[i]}"
                    f"Estado: {datos.equipos_estados[i]}"
                )

    if opcion == "3":
        print("Programa finaliado")

    else:
        print("Opción inválida. Intente nuevamente.")

