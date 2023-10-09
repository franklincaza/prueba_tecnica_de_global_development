def filtrar_numeros(lista):
    """
Escriba una función que retorne en una lista de salida, solo aquellos números de una lista de entrada que satisfagan las
siguientes condiciones:
1. El número debe ser divisible por cinco.
2. Si el número es mayor que 600, no se incluye en la salida.
3. Si el número es mayor que 1000, detenga el procesamiento y retorne el resultado.
Ejemplos:
Entrada : [24, 150, 300, 660, 295, 1050, 50]
Salida : [150, 300, 295]
Entrada : [110, 720, 307, 555, 1095, 12, 300, 1000]
Salida : [110, 555]

    """
    resultado = []

    for numero in lista:
        if numero > 1000:
            return resultado
        if numero % 5 == 0 and numero <= 600:
            resultado.append(numero)

    return resultado

# Ejemplos
entrada1 = [24, 150, 300, 660, 295, 1050, 50]
salida1 = filtrar_numeros(entrada1)
print(salida1)  # Salida: [150, 300, 295]

entrada2 = [110, 720, 307, 555, 1095, 12, 300, 1000]
salida2 = filtrar_numeros(entrada2)
print(salida2)  # Salida: [110, 555]
