def agrupar_elementos_similares(lista):
    """
Ejercicio 3.
Dada una lista de cualquier longitud de entrada, escriba una función para agrupar los elementos similares en una matriz
de salida (no importa el orden). Ejemplos:
Entrada : list = [12, 25, 1, 1, 7, 25]
Salida : [[12], [7], [25, 25], [1, 1]]
Entrada : list = [6, 7, 8, 9]
Salida : [[6], [7], [8], [9]]

    """
    grupos = []
    elementos_procesados = set()

    for elemento in lista:
        if elemento not in elementos_procesados:
            grupo = [elem for elem in lista if elem == elemento]
            grupos.append(grupo)
            elementos_procesados.add(elemento)

    return grupos

# Ejemplos
entrada1 = [12, 25, 1, 1, 7, 25]
salida1 = agrupar_elementos_similares(entrada1)
print(salida1)  # Salida: [[12], [25, 25], [1, 1], [7]]

entrada2 = [6, 7, 8, 9]
salida2 = agrupar_elementos_similares(entrada2)
print(salida2)  # Salida: [[6], [7], [8], [9]]
