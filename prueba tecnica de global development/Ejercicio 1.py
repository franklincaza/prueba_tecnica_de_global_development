def suma_serie(numero, terminos):
    """
Ejercicio 1.
Escriba una función que retorne la suma de una serie de X número repetido hasta el n-ésimo término. Ejemplos:
Entrada : numero=3, terminos=5
Salida : 37035 #(3 + 33 + 333 + 3333 + 33333)
Entrada : numero=5, terminos=3
Salida : 615 #(5 + 55 + 555)
    """
    resultado = 0
    termino_actual = 0

    for i in range(terminos):
        termino_actual = termino_actual * 10 + numero
        resultado += termino_actual

    return resultado

# Ejemplos
resultado1 = suma_serie(3, 5)
print(resultado1)  # Salida: 37035

resultado2 = suma_serie(5, 3)
print(resultado2)  # Salida: 615
