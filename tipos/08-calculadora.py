n1 = input("Ingresa primer numero: ")
n2 = input("Ingresa segundo numero: ")

n1 = int(n1)
n2 = int(n2)

# print("La suma es: " + str(n1 + n2))
# print(f"La suma es: {n1 + n2}")

suma = n1+n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los mensajes números {n1} y {n2},
El resultado de la suma es {suma}
El resultado de la resta es {resta}
El resultado de la multiplicación es {multi}
El resultado de la división es {div}
"""
print(mensaje)
