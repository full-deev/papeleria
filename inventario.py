# ==========================================
# SISTEMA DE INVENTARIO PARA UNA PAPELERÍA
# Desarrollado por: Camilo Sandoval
# Proyecto Integrador
# ==========================================

# Lista donde se almacenarán todos los productos
inventario = []

# Variable que controla el menú principal
opcion = 0

# El ciclo se ejecutará hasta que el usuario decida salir
while opcion != 6:

    # Mostrar el menú principal
    print("\n==============================")
    print(" SISTEMA DE INVENTARIO ")
    print("==============================")
    print("1. Registrar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar stock")
    print("5. Eliminar producto")
    print("6. Salir")

    # Solicitar la opción al usuario
    opcion = int(input("Seleccione una opción: "))

    # Registrar un nuevo producto
    if opcion == 1:

        print("\nREGISTRO DE PRODUCTO")

        codigo = input("Código: ")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))

        # Crear una lista con los datos del producto
        producto = [codigo, nombre, precio, cantidad]

        # Guardar el producto dentro del inventario
        inventario.append(producto)

        print("\nProducto registrado correctamente.")