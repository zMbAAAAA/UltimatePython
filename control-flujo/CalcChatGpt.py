def bienvenida():
    print("¡Bienvenido al programa de operaciones matemáticas!")


def solicitar_numero(mensaje):
    return float(input(mensaje))


def solicitar_operacion():
    return input("Por favor, elija la operación a realizar (suma, resta, multi, divi): ").strip().lower()


def realizar_operacion(numero1, operacion, numero2):
    if operacion == "suma":
        return numero1 + numero2
    elif operacion == "resta":
        return numero1 - numero2
    elif operacion == "multi":
        return numero1 * numero2
    elif operacion == "divi":
        if numero2 == 0:
            print("Error: División por cero.")
            return None
        return numero1 / numero2
    else:
        print("Operación no válida. Inténtelo de nuevo.")
        return None


def main():
    bienvenida()

    numero1 = solicitar_numero("Por favor, ingrese un número: ")

    while True:
        operacion = solicitar_operacion()
        numero2 = solicitar_numero("Por favor, ingrese el segundo número: ")

        resultado = realizar_operacion(numero1, operacion, numero2)

        if resultado is not None:
            print(f"El resultado de la {operacion} es: {resultado}")
            # Almacenar el resultado como el primer número para la siguiente iteración
            numero1 = resultado


if __name__ == "__main__":
    main()
