# Simulador de máquina de Turing

![Python](https://img.shields.io/badge/language-Python-blue)
![Automata theory](https://img.shields.io/badge/topic-Automata%20Theory-green)
![Turing machine](https://img.shields.io/badge/model-Turing%20Machine-orange)

Simulación interactiva de una máquina de Turing que evalúa palabras basadas en un conjunto de transiciones definidas por el usuario.

## Características

- Permite configurar estados iniciales y finales.
- Admite transiciones en formato `d(q,x) = (p,Y,L)`:
  - `q`: estado actual
  - `x`: símbolo actual en la cinta
  - `p`: nuevo estado
  - `Y`: símbolo reemplazado
  - `L`: movimiento del cabezal (`I` para izquierda, `D` para derecha)
- Verifica si las palabras pertenecen al lenguaje.

## Versiones disponibles

1. **Con interfaz gráfica (GUI):** experiencia visual amigable.  
2. **Sin interfaz gráfica (CLI):** ejecución en consola, más ligera.  
3. **Jupyter notebook:** para simulaciones paso a paso.

## Requisitos

- **Sistema operativo:** Windows (para ejecutables).
- **Python:** versión 3.x (para ejecutar los scripts).

## Ejecución

- **GUI:** abre `turing-gui.exe`. Código fuente en `turing-gui.py`.
- **CLI:** abre `turing-cli.exe`. Código fuente en `turing-cli.py`.
- **Notebook:** abre `turing-simulador.ipynb` y ejecuta los bloques de código.

## Ejemplo de salida

```plaintext
Ingrese el estado inicial: q0
Ingrese el estado final: qf

Ingrese el número de transiciones: 2

----- Transición 1 -----
Ingrese q: q0
Ingrese x: a
Ingrese p: q1
Ingrese Y: X
Ingrese L: D
d( q0 , a ) = ( q1 , X , D )

----- Transición 2 -----
Ingrese q: q1
Ingrese x: B
Ingrese p: qf
Ingrese Y: B
Ingrese L: I
d( q1 , B ) = ( qf , B , I )

Ingrese palabra ('exit' para salir): a
La palabra a SI pertenece al lenguaje especificado.

Ingrese palabra ('exit' para salir): b
La palabra b NO pertenece al lenguaje especificado.

Ingrese palabra ('exit' para salir): exit
Programa finalizado.