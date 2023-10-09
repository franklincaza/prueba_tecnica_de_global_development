# Listas para almacenar productos y existencias por grupo
#dairy_products = ["Fairlife Milk", "Alta Dena Milk", "Queensland Butter"]
#cleaning_products = ["Product1", "Product2", "Product3"]
#grain_products = ["Product4", "Product5", "Product6"]
dairy_products = []
cleaning_products = []
grain_products = []

#dairy_stock = [28, 36, 50]
#cleaning_stock = [10, 20, 30]
#grain_stock = [5, 15, 25]

dairy_stock = []
cleaning_stock = []
grain_stock = []

# Función para agregar o actualizar productos en el inventario
def agregar_producto(nombre, cantidad, grupo):
    if grupo == 'dairy':
        if nombre in dairy_products:
            indice = dairy_products.index(nombre)
            dairy_stock[indice] += cantidad
        else:
            dairy_products.append(nombre)
            dairy_stock.append(cantidad)
    elif grupo == 'cleaning':
        # Realiza un procedimiento similar para el grupo 'cleaning'
        pass
    elif grupo == 'grain':
        # Realiza un procedimiento similar para el grupo 'grain'
        pass
    else:
        print("Grupo no válido")

# Función para mostrar el reporte de inventario
def mostrar_inventario():
    print("Nombre\t\t\t\tExistencias")
    print("-" * 40)
    
    for i in range(len(dairy_products)):
        print(f"{dairy_products[i]}\t\t\t\t{dairy_stock[i]}")
    
    for i in range(len(cleaning_products)):
        # Mostrar productos del grupo 'cleaning'
        pass
    
    for i in range(len(grain_products)):
        # Mostrar productos del grupo 'grain'
        pass

# Menú principal del programa
while True:
    print("-" * 70)
    print("Sistema de inventarios. Ingrese una opción:")
    print("-" * 70)
    print("1. Agregar producto.")
    print("2. Ver reporte de inventario.")
    print("3. Salir.")
    
    opcion = input("Su opción: ")
    
    if opcion == '1':
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        grupo = input("Ingrese el grupo (dairy, cleaning, grain): ")
        agregar_producto(nombre, cantidad, grupo)
        print("Producto agregado al inventario.")
    elif opcion == '2':
        mostrar_inventario()
    elif opcion == '3':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")


