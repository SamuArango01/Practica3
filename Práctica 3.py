from nltk import CFG, ChartParser, Tree
import re

# Definir la gramática en formato BNF
gramatica = CFG.fromstring("""
    E -> E '+' T | E '-' T | T
    T -> T '*' F | T '/' F | F
    F -> '(' E ')' | 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' | '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
""")

# Tokenizar la entrada
def tokenizar(entrada):
    # Divide operadores, paréntesis y variables/dígitos en tokens separados
    return re.findall(r'[a-zA-Z0-9]+|[()+\-*/]', entrada)

# Leer la expresión objetivo desde consola
entrada = input("Ingrese la expresión a derivar: ")
expresion_objetivo = tokenizar(entrada)

# Preguntar si se desea derivar por la izquierda o por la derecha
direccion = input("Seleccione la derivación (i para izquierda, d para derecha): ").strip().lower()

# Función para derivación explícita
def derivar(gramatica, expresion_objetivo, direccion):
    pasos = []

    # Modificar orden de las reglas según la dirección
    if direccion == 'i':
        gramatica = CFG.fromstring("""
            E -> T '+' E | T '-' E | T
            T -> F '*' T | F '/' T | F
            F -> '(' E ')' | 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' | '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
        """)
    elif direccion == 'd':
        gramatica = CFG.fromstring("""
            E -> E '+' T | E '-' T | T
            T -> T '*' F | T '/' F | F
            F -> '(' E ')' | 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' | '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
        """)

    # Parser con la gramática ajustada
    parser = ChartParser(gramatica)

    for tree in parser.parse(expresion_objetivo):
        pasos.append(tree)  # Guardar árboles generados
    return pasos

# Función para generar el AST
def generar_ast(arbol):
    if arbol.height() <= 2:  # Nodo hoja
        return arbol
    elif arbol.label() in ["E", "T", "F"]:  # Eliminar reglas intermedias
        return Tree(arbol.label(), [generar_ast(hijo) for hijo in arbol if isinstance(hijo, Tree)])
    return arbol

# Valida la entrada del usuario y muestra derivaciones
if direccion in ["i", "d"]:
    print(f"\nDerivación por la {'izquierda' if direccion == 'i' else 'derecha'}:")

    for arbol in derivar(gramatica, expresion_objetivo, direccion):
        print("\nÁrbol de derivación:")
        arbol.pretty_print()  # Muestra el árbol en consola
        arbol.draw()  # Muestra el árbol con la I.G.(Interfaz Gráfica)

        # Generar AST y mostrarlo
        ast = generar_ast(arbol)
        print("\nÁrbol Sintáctico Abstracto (AST):")
        print(ast)
        ast.draw()  # Muestra el AST gráficamente
else:
    print("Ingresaste incorrectamente. Por favor, ingrese 'i' para izquierda o 'd' para derecha.")
