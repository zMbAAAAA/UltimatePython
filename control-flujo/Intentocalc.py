m1 = input("Ingresa número: ")
m3 = input("Ingresa operación, (suma, resta, mu): ")
m2 = input("Ingresa siguiente número: ")

m1 = int(m1)
m2 = int(m2)
m3 = str(m3)

if m3 == "suma":
    result = m1 + m2
    print(result)
elif m3 == "resta":
    result = m1 - m2
    print(result)
elif m3 == "multi":
    result = m1 * m2
    print(result)
else:
    result = m1 / m2
    print(result)

result = m1
