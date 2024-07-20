animal = "  chanCHito feliz  "
print(animal.upper())  # Convierte todo en mayúsculas
print(animal.lower())  # Convierte todo en minúsculas
print(animal.capitalize())  # Convierte la primera letra en mayúscula
# Strip y capitalize quita los espacios y convierte la primera letra en mayúscula
print(animal.strip().capitalize())
# Convierte las primeras las letras de cada palabra en mayúscula
print(animal.title())
print(animal.strip())  # Strip quita los espacios
print(animal.lstrip())  # Strip quita los espacios de la izquierda
print(animal.rstrip())  # Strip quita los espacios de la derecha
print(animal.find("cH"))  # Busca que numero el índice en el string
print(animal.replace("nCH", "j"))  # Reemplaza unos carácteres por
# Busca si la cadena de carácteres se encuentra dentro del string
print("nCH" in animal)
# Busca si la cadena de carácteres no se encuentra dentro del string
print("nCH" not in animal)
print("nCH" in animal)
