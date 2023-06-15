def agregaNombre():
    archivo = open("nombres.txt", "w")
    telefonos = open("telefonos.txt", "w")
    numNombres = int(input("Ingrese la cantidad que quiere agregar: "))
    count = 0

    while count < numNombres:
        nombre = input("Ingrese un nombre: ")
        telefono = input("Ingrese el numero celular: ")
        archivo.write(nombre)
        archivo.write("\n")
        telefonos.write(telefono)
        telefonos.write("\n")
        count = count + 1

    archivo.close()
    telefonos.close()
    leeNombre()
    seguirAgregando()


def buscaNombre():
    archivo = open("nombres.txt", "r")
    telefonos = open("telefonos.txt", "r")
    buscaNombre = input("Ingrese el nombre a buscar: ")
    encontrado = False
    nombres = []
    telefonosList = []
    count = 0

    for nombre in archivo.readlines():
        nombre = nombre.strip().lower()
        nombres.append(nombre)

    for telefono in telefonos.readlines():
        telefono = telefono.strip()
        telefono = int(telefono)
        telefonosList.append(telefono)

    for nombre in nombres:
        count = count+1
        if nombre == buscaNombre:
            encontrado = True
            break

    if encontrado:
        print("El nombre existe y su celular es ", telefonosList[count-1])
    else:
        print("El nombre no existe")
        
    telefonos.close()
    archivo.close()
    seguirAgregando()

def leeNombre():
    archivo = open("nombres.txt", "r")
    print("Usted agrego los siguientes nombres: ")
    for nombre in archivo.readlines():
        nombre = nombre.strip().lower()
        print(nombre)

    archivo.close()

def opciones():
    
    opcion = input("Ingrese la opcion 1 para agregar y 2 para buscar: ")

    if opcion == "1":
        agregaNombre()
    elif opcion =="2":
        buscaNombre()

def seguirAgregando():
    respuesta = input("Para salir escriba (Salir) sino de enter: ")

    if respuesta.lower() != "salir":
        opciones()

opciones()