import datos
import operaciones

codigo = input ("Ingrese el código del equipo: ").strip().upper()
tipo = input ("Ingrese el tipo: Desktop, Notebook, Monitos o Celular ").strip()

operaciones.registrar_equipo(codigo, tipo)

