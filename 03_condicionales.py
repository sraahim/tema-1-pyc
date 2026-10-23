"""Sesión 3 — Estructuras de control condicionales (A.1.2)

    if / elif / else, condiciones anidadas, operador ternario.
    Práctica: clasificar un movimiento según signo (ingreso/gasto/cero) y avisar de saldo negativo.
    Producto: 03_condicionales.py."""

IVA =0.21 #21 % de IVA (constante)
DESCUENTO = 0.10 #10 % de descuento 
print("=== Registro de un movimiento ===")

importe_bruto = float(input("Importe bruto (EUR): "))

importe = float(input("Importe bruto (EUR): (positivo para ingreso, negativo para gesto): "))

if importe < 0:
    tipo = "gasto"
elif importe > 0:
    tipo = "ingreso"
else: 
    tipo = "neutro"

signo = "+" if importe >= 0 else ""

print(f"Tipo de movimiento: {tipo}")
print(f"Importe: {signo}{importe:.2f}EUR")

saldo_actual = float(input("Ingrese su saldo actual (EUR):"))
saldo_resultante = saldo_actual + importe


if tipo == "gasto":
    if saldo_resultante < 0:
        print(f"¡Atención! Su saldo restante es negativo")
    elif saldo_resultante == 0:
        print("¡Atención! Su saldo restante es cero")
    else:
        print("¡Atención! Su saldo restante es positivo!")
else:
    print(f"Su saldo resultante es{saldo_resultante} EUR")
