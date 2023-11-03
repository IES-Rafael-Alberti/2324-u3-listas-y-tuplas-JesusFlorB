"""Escribir un programa que almacene las matrices A=(123456) y B=(-100111) en una lista y muestre por pantalla su producto. 
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista."""

def multiplicar_matrices(matriz1, matriz2):
    #Esta funcion multiplica dos matrices.s
    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    columnas_matriz2 = len(matriz2[0])

    if columnas_matriz1 != filas_matriz2:
        raise ValueError("El numero de columnas de la primera matriz debe ser igual al numero de filas de la segunda matriz.")

    resultado = [[0 for _ in range(columnas_matriz2)] for _ in range(filas_matriz1)]

    for i in range(filas_matriz1):
        for j in range(columnas_matriz2):
            for k in range(filas_matriz2):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

if __name__ == "__main__":
    matriz_A = [[1, 2, 3], [4, 5, 6]]
    matriz_B = [[-1, 0, 0], [1, 1, 1], [1, 1, 1]]

    try:
        resultado = multiplicar_matrices(matriz_A, matriz_B)
        print("El resultado de la multiplicacion es:")
        for fila in resultado:
            print(fila)
    except ValueError as e:
        print(e)