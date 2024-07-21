buscar = 2
for numero in range(11):
    print(numero)
    if numero == buscar:
        print("Encontrado:", buscar)
        break
else:
    print("no encontré el número buscado :(")
