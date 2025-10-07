import random

GREEN_BG = "\033[42m"
YELLOW_BG = "\033[43m"
GRAY_BG = "\033[47m"
RESET = "\033[0m"

def colorear_letra(letra: str, estado: str) -> str :
    """La función recibe una letra y un estado y devuelve la letra coloreada.

    Cambié el formato para que el carácter coloreado sea exactamente la letra
    (sin espacio extra). Esto evita que el código RESET quede separado del
    bloque de color y provoque que el color del terminal no se restablezca
    correctamente.
    """
    ch = letra.upper()
    if estado == "verde":
        return f"{GREEN_BG}{ch}{RESET}"
    elif estado == "amarillo":
        return f"{YELLOW_BG}{ch}{RESET}"
    else:
        return f"{GRAY_BG}{ch}{RESET}"

# TODO_____________________

def elegir_palabra(palabras: list[str]) -> str: 
    """
    Selecciona aleatoriamente la palabra del día de la lista de palabras.

    Parámetros:
        palabras (list): lista de palabras en mayúsculas

    Retorna:
        str: palabra seleccionada
    """
    if not palabras:
        raise ValueError("La lista de palabras está vacía")
    return random.choice(palabras)


def comprobar_intento(palabra_secreta: str, intento: str):
    """
    Compara el intento con la palabra secreta y devuelve una lista indicando
    para cada letra si es:
        - "verde" -> letra correcta y en la posición correcta
        - "amarillo" -> letra presente en otra posición
        - "gris" -> letra no presente

    Parámetros:
        palabra_secreta (str): palabra a adivinar
        intento (str): intento del jugador

    Retorna:
        list[str]: lista de estados por letra
    """
    # Normalizamos a mayúsculas
    palabra_secreta = palabra_secreta.upper()
    intento = intento.upper()

    resultado: list[str] = ["gris"] * len(intento)

    # Contador de letras de la palabra secreta para manejar repetidas
    letras_secreta: dict[str, int] = {}
    for ch in palabra_secreta:
        letras_secreta[ch] = letras_secreta.get(ch, 0) + 1

    # Primera pasada: marcar verdes
    for i, ch in enumerate(intento):
        if i < len(palabra_secreta) and ch == palabra_secreta[i]:
            resultado[i] = "verde"
            letras_secreta[ch] -= 1

    # Segunda pasada: marcar amarillos
    for i, ch in enumerate(intento):
        if resultado[i] == "verde":
            continue
        if ch in letras_secreta and letras_secreta[ch] > 0:
            resultado[i] = "amarillo"
            letras_secreta[ch] -= 1
        else:
            resultado[i] = "gris"

    return resultado


def mostrar_feedback(intento, resultado):
    """
    Muestra el intento en la consola con feedback de colores.

    Parámetros:
        intento (str): palabra intentada
        resultado (list[str]): lista con estados por letra ("verde", "amarillo", "gris")

    Ejemplo:
        intento = "CASA"
        resultado = ["amarillo", "gris", "gris", "verde"]
        => se muestra cada letra con el color correspondiente
    """
    # Mostrar cada letra coloreada usando colorear_letra
    partes: list[str] = []
    for letra, estado in zip(intento, resultado):
        partes.append(colorear_letra(letra, estado))
    # Asegurarnos de que al final imprimimos RESET para restaurar atributos
    # del terminal aunque la última letra sea verde.
    print("".join(partes) + RESET)


def validar_intento(intento, palabras):
    """
    Valida que el intento:
      - tenga 5 letras
      - esté en la lista de palabras cargadas

    Parámetros:
        intento (str): intento del jugador
        palabras (list): lista de palabras válidas

    Retorna:
        bool: True si es válido, False si no
    """
    import unicodedata

    if not isinstance(intento, str):
        return False
    intento = intento.strip()
    # eliminar tildes y pasar a mayúsculas
    intento = ''.join(
        c for c in unicodedata.normalize('NFD', intento)
        if unicodedata.category(c) != 'Mn'
    ).upper()

    if len(intento) != 5:
        return False
    # Debe estar en la lista de palabras válidas (ignorar mayúsc/minúsc)
    return intento in (w.upper() for w in palabras)


# Esto solo se ejecuta si ejecutamos esta librería directamente
# pero no si la importamos en otro fichero
if __name__ == "__main__":

  palabra = "carta"
  intento = "casas"

  resultado = []
  for i, letra in enumerate(intento):
      if letra == palabra[i]:
          resultado.append(colorear_letra(letra, "verde"))
      elif letra in palabra:
          resultado.append(colorear_letra(letra, "amarillo"))
      else:
          resultado.append(colorear_letra(letra, "gris"))

  print("".join(resultado))


