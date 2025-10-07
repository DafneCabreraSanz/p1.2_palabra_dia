import carga_palabras
from wordle_funciones import (
	elegir_palabra,
	comprobar_intento,
	mostrar_feedback,
	validar_intento,
	colorear_letra,
)

# Programa principal
def main() -> None:
	# Cargar palabras y elegir la palabra secreta
	palabras = carga_palabras.cargar_palabras("palabras_5.txt")
	palabra_secreta = elegir_palabra(palabras)

	print("Palabra del día: ?????")
	print("Tienes 6 intentos.\n")

	# Bucle de intentos
	intentos_max = 6
	# contador de intentos
	for intento_num in range(1, intentos_max + 1):
		while True:
			entrada = input(f"Intento {intento_num}: ").strip()
			# normalizar tildes y pasar a mayúsculas se hace en la carga/validación
			if validar_intento(entrada, palabras):
				intento = entrada.strip().upper()
				break
			else:
				# Mensajes de error específicos
				if len(entrada) != 5:
					print("Error: solo se permiten palabras de 5 letras")
				else:
					print("Error: palabra no válida (no está en la lista)")
	# Comprobar intento y mostrar feedback
		resultado = comprobar_intento(palabra_secreta, intento)
		mostrar_feedback(intento, resultado)
		# Comprobar si ha ganado
		if all(r == "verde" for r in resultado):
			print(f"\n¡Felicidades! Has acertado la palabra: {palabra_secreta}")
			return

	print(f"\nSe han agotado los intentos. La palabra era: {palabra_secreta}")


if __name__ == "__main__":
	main()

