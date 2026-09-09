import datos
import operaciones

codigo = input ("Ingrese el código del equipo: ").strip().upper()
tipo = input ("Ingrese el tipo: Desktop, Notebook, Monitos o Celular ").strip()

operaciones.registrar_equipo(codigo, tipo) #Valida los datos y registra el equipo si son correctos.

print("Códigos registrados:", datos.equipos_codigos)
print("Tipos registrados:", datos.equipos_tipos)
print("Estados registrados:", datos.equipos_estados)
print("Legajos registrados:", datos.equipos_legajos)

