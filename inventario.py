# SISTEMA DE INVENTARIO PARA UNA PAPELERÍA
# Proyecto Integrador

# Lista donde se almacenarán todos los productos
inventario = []

# Variable que controla el menú
opcion = 0

# El programa seguirá ejecutándose hasta que el usuario elija salir
while opcion != 5:

    print("\n===================================")
    print(" SISTEMA DE INVENTARIO PAPELERÍA")
    print("1. Registrar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = int(input("\nSeleccione una opción: "))

    # OPCIÓN 1 - REGISTRAR PRODUCTO
    if opcion == 1:
        print("\n--- REGISTRAR PRODUCTO ---")
        codigo = input("Código: ")
        # Verificar si el código ya existe
        existe = False

        for producto in inventario:
            if producto[0] == codigo:
                existe = True
        if existe == True:
            print("Ese código ya está registrado.")
        else:
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            # Crear la lista del producto
            producto = [codigo, nombre, precio, cantidad]
            # Guardar en el inventario
            inventario.append(producto)
            print("Producto registrado correctamente.")

    # OPCIÓN 2 - MOSTRAR INVENTARIO
    elif opcion == 2:
        print("\n------- INVENTARIO -------1")
        if len(inventario) == 0:
            print("No existen productos registrados.")

        else:

            print("------------------------------------------------------------")
            print("CODIGO\tNOMBRE\t\tPRECIO\tCANTIDAD")
            print("------------------------------------------------------------")

            for producto in inventario:
                print(
                    producto[0], "\t",
                    producto[1], "\t\t",
                    producto[2], "\t",
                    producto[3]
                )

    # OPCIÓN 3 - BUSCAR PRODUCTO
    elif opcion == 3:
        print("\n--- BUSCAR PRODUCTO ---")
        codigo = input("Ingrese el código: ")
        encontrado = False

        for producto in inventario:
            if producto[0] == codigo:

                print("\nProducto encontrado")
                print("-------------------------")
                print("Código:", producto[0])
                print("Nombre:", producto[1])
                print("Precio:", producto[2])
                print("Cantidad:", producto[3])

                encontrado = True

        if encontrado == False:
            print("Producto no encontrado.")

    # OPCIÓN 4 - ELIMINAR PRODUCTO
    elif opcion == 4:
        print("\n--- ELIMINAR PRODUCTO ---")
        codigo = input("Ingrese el código del producto: ")
        encontrado = False

        for producto in inventario:
            if producto[0] == codigo:
                inventario.remove(producto)
                encontrado = True
                print("Producto eliminado correctamente.")
                break

        if encontrado == False:
            print("Producto no encontrado.")

    # OPCIÓN 5 - SALIR
    elif opcion == 5:
        print("\nGracias por utilizar el sistema.")
        print("Hasta luego.")
    # OPCIÓN INVÁLIDA
    else:
        print("Opción incorrecta.")