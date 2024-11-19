## **Practica** #3
## **Autores**
Este proyecto fue desarrollado por:
- **Mateo Sanz**
- **Samuel Arango**

# Generador de Derivaciones y Árboles Sintácticos (AST)

Este proyecto es un generador de derivaciones basado en gramáticas libres de contexto (CFG), que permite representar gráficamente tanto los árboles de derivación como los árboles sintácticos abstractos (AST). El programa es capaz de realizar derivaciones por la izquierda o por la derecha según lo seleccionado por el usuario.

## **Características**
- Permite ingresar una gramática en formato BNF.
- Deriva expresiones ingresadas por consola usando derivación por la izquierda o por la derecha.
- Genera y muestra árboles de derivación de manera gráfica.
- Construye un Árbol Sintáctico Abstracto (AST) simplificado a partir de las derivaciones.
- Compatible con expresiones aritméticas básicas y símbolos definidos por la gramática.

## **Requisitos**
1. Python 3.8 o superior.
2. Biblioteca **`nltk`** instalada. Si no está instalada, puedes hacerlo con:
   ```bash
   pip install nltk
   ```

## **Uso**
1. Clona el repositorio:
   ```bash
   git clone https://github.com/SamuArango01/Practica3.git
   cd generador-derivaciones-ast
   ```

2. Ejecuta el programa:
   ```bash
   python main.py
   ```

3. Sigue las instrucciones en la consola:
   - Ingresa la expresión que deseas derivar, separando los tokens por espacios.
   - Elige el tipo de derivación:
     - **`i`**: Derivación por la izquierda.
     - **`d`**: Derivación por la derecha.

4. El programa mostrará en consola:
   - El árbol de derivación.
   - El Árbol Sintáctico Abstracto (AST).
   Además, abrirá ventanas gráficas con las visualizaciones de los árboles.

### **Ejemplo**
**Gramática definida en el programa:**
```plaintext
E -> E '+' T | E '-' T | T
T -> T '*' F | T '/' F | F
F -> '(' E ')' | 'a' | 'b' | ... | 'z' | '0' | '1' | ... | '9'
```

**Entrada del usuario:**
```plaintext
Ingrese la expresión que deseas derivar: 4 + ( a - b ) * x
Seleccione la derivación (i para izquierda, d para derecha): i
```

**Salida:**
- Árbol de derivación mostrado en consola y en ventana gráfica.
- AST mostrado en consola y en ventana gráfica.

## **Estructura del proyecto**
- `main.py`: Código principal del programa.
- `README.md`: Instrucciones y descripción del proyecto.
- `requirements.txt`: Archivo con dependencias requeridas (si se utilizan bibliotecas adicionales).


