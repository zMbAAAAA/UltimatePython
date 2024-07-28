print("*    Bienvenido al cálculo de números")
print("*    Para salir puedes escribir SALIR")
print("*    Las operaciones son (suma, resta, multiplicación y división) ")

n1 = ""
while True:
    if not n1:
        n1 = input("Ingrese primer número: ")
        if n1.lower() == "salir":
            break
        n1 = int(n1)
    op = input("Ingrese el tipo de operacion: ")
    if op.lower() == "salir":
        break

    n2 = input("Ingrese el segundo número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower
