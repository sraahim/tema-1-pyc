"""Sesión 1 — Elementos básicos del lenguaje (A.1.1)

    Tipos básicos de datos (int, float, str, bool), constantes y variables, input(), print().
    Operadores aritméticos, de comparación y lógicos; expresiones y f-strings.
    Comentarios y estilo PEP 8.
    Práctica: "Ficha de bienvenida": pedir nombre y saldo inicial y mostrarlos formateados.
    Producto: 01_basicos.py."""

nombre = input("introduca su nombre :")
apellidos = input("introduca sus apellidos :")
saldo = float(input("intoduzca su saldo inicial : "))



print(f"Nombre: (nombre)")
print(f"Apellidos: (apellidos)")
print(f"Saldo Inicial: (saldo)")