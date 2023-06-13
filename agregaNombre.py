def agregaNombre():
    archivo = open("nombres.txt", "w")
    numNombres = input("Si no quiere agregar mas nombres ingrese listo")

    while numNombres != "listo":
        nombre = input("Ingrese un numbre")
        archivo.write(nombre)
        archivo.write("\n")
        numNombres = input("Si no quiere agregar mas nombres ingrese listo")

    archivo.close()


def buscaNombre():
    archivo = open("nombres.txt", "r")
    buscaNombre = input("Ingrese el nombre a buscar")
    encontrado = False
    for nombre in archivo.readlines():
        nombre = nombre.strip().lower()
        if buscaNombre.lower() == nombre:
            encontrado = True

    if encontrado:
        print("El nombre existe")
    else:
        print("El nombre no existe")

    archivo.close()

opcion = input("Ingrese la opcion 1 para agregar y 2 para buscar")

if opcion == "1":
    agregaNombre()
elif opcion =="2":
    buscaNombre()