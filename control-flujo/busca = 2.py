# buscar = 2
# numeros = range(11)

# if buscar in numeros:
#     print("Encontrado:", buscar)
# else:
#     print("No encontré el número buscado :(")


buscar = 2

if any(numero == buscar for numero in range(11)):
    print("Encontrado:", buscar)
else:
    print("No encontré el número buscado :(")


buscar = 2
numeros = range(11)


if buscar in numeros:
    print("Encontrado:", buscar)
else:
    print("No encontré el número buscado :(")
