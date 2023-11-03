from src.ejercicio12 import multiplicar_matrices

def test_multiplicar_matrices():
    matriz_A = [[1, 2, 3], [4, 5, 6]]
    matriz_B = [[-1, 0, 0], [1, 1, 1], [1, 1, 1]]

    resultado_esperado = [[4, 5, 5], [7, 11, 11]]

    try:
        resultado = multiplicar_matrices(matriz_A, matriz_B)
        assert resultado == resultado_esperado
    except ValueError as e:
        assert str(e) == "El numero de columnas de la primera matriz debe ser igual al numero de filas de la segunda matriz."