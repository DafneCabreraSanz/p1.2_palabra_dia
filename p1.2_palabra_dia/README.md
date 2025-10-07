# Práctica 1.2 : Implementar un juego: “Palabra del día” (Wordle)

## Objetivo

Implementar un juego tipo **Wordle** en consola usando Python.  
Si nunca habéis jugado podéis echar una partida para comprender su funcionamiento: [Palabra del día](https://lapalabradeldia.com/)
El jugador debe adivinar una **palabra secreta de 5 letras** en un número limitado de intentos, recibiendo pistas sobre letras correctas en la posición correcta o letras presentes en otra posición.

### Ficheros proporcionados:

- `carga_palabras.py`: Este módulo contiene una función que carga las palabras de un fichero de texto, quita las tildes y pasa todo a mayúsculas.
- `wordle_funciones.py`: Aquí tendremos que implementar las funciones que contienen la **lógica del juego**. Ya contiene una función que nos ayuda a mostrar las letras con un fondo de color.
- `main.py` → ejecuta el juego.
- `palabras_5.txt` → fichero con todas las palabras de 5 letras, **una por línea**.

## Requisitos de la práctica

1. **Carga de palabras**

   - Usar la función `cargar_palabras` del módulo `carga_palabras.py` para cargar todas las palabras de 5 letras.
   - Todas las palabras deben quedar **en mayúsculas y sin tildes**.

2. **Funciones del juego** (`wordle_funciones.py`)  
   Implementar al menos las siguientes funciones:

   - `elegir_palabra(palabras: list) -> str`

     - Selecciona aleatoriamente la palabra del día.

   - `comprobar_intento(palabra_secreta: str, intento: str) -> list`

     - Devuelve una lista indicando para cada letra si es:
       - `"verde"` → correcta y en la posición correcta
       - `"amarillo"` → letra presente pero en otra posición
       - `"gris"` → letra no presente

   - `mostrar_feedback(intento: str, resultado: list)`

     - Muestra el intento en la consola **con cuadros de colores** según el resultado (pueden usar ANSI o emojis).

   - (Opcional) Funciones auxiliares para validar entradas, contar intentos, etc.

3. **Main** (`main.py`)

   - Ejecuta el juego completo:
     1. Carga todas las palabras usando `cargar_palabras`.
     2. Elige aleatoriamente la palabra del día.
     3. Permite al jugador realizar hasta 6 intentos.
     4. Repetiremos el intento hasta que el usuariio introduzca una palabra válida.
     5. Después de cada intento, muestra el feedback coloreado.
     6. Termina el juego si el jugador acierta o se agotan los intentos, mostrando la palabra secreta.

4. **Validaciones**

   - Solo se aceptan palabras de 5 letras que estén en la lista cargada.
   - Ignorar tildes y pasar entradas a mayúsculas automáticamente.

5. **Utilizar Type Hints.**: 
   - Indicar los tipos de las variables.
   - Indicar los tipos de los parámetros que reciven las funciones y los tipos devueltos.
   
6. **Extras opcionales (para quien quiera complicarlo)**
   - Contador de victorias/derrotas.
   - Guardar el historial de intentos en un fichero.
   - Animaciones sencillas con emojis o colores.
   - Permitir jugar varias rondas sin reiniciar el programa.

---

## Ejemplo de ejecución (en consola)

```shell
Palabra del día: ?????
Tienes 6 intentos.

Intento 1: CASAS
🟨 M 🟩 A ⬜ Z 🟩 A 🟩 S

Intento 2: CAMA
Error: solo se permiten palabras de 5 letras

Intento 2: CAMAS
🟩 C 🟩 A 🟩 M 🟩 A 🟩 S

¡Felicidades! Has acertado la palabra: CAMAS
```
