# Inicializar diccionarios para los grupos de productos y sus existencias
inventory = {
    "dairy": {},
    "cleaning": {},
    "grain": {}
}

# Función para agregar un producto al inventario
def agregar_producto():
    grupo = input("Ingrese el grupo del producto (dairy, cleaning, grain): ").lower()
    nombre_producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))

    # Verificar si el grupo existe en el inventario
    if grupo in inventory:
        # Verificar si el producto ya existe en el grupo
        if nombre_producto in inventory[grupo]:
            inventory[grupo][nombre_producto] += cantidad
        else:
            inventory[grupo][nombre_producto] = cantidad
        print(f"Producto '{nombre_producto}' agregado al grupo '{grupo}' con una cantidad de {cantidad}.")
    else:
        print("Grupo de producto no válido. Producto no agregado.")

# Función para ver el reporte de inventario
def ver_reporte_inventario():
    print("Reporte de inventario:")
    for grupo, productos in inventory.items():
        print(f"Grupo: {grupo}")
        for producto, existencias in productos.items():
            print(f"- {producto}: {existencias} unidades")
    print("\n")

# Función principal
while True:
    print("-------------------------------------------------------------------------")
    print("Sistema de inventarios. Ingrese una opción:")
    print("-------------------------------------------------------------------------")
    print("1. Agregar producto.")
    print("2. Ver reporte de inventario.")
    print("3. Salir.")
    print("-------------------------------------------------------------------------")

    opcion = input("Opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        ver_reporte_inventario()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

