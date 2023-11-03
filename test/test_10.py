from src.ejercicio10 import encontrar_menor_mayor_precios

def test_encontrar_menor_mayor_precios():
    menor, mayor = encontrar_menor_mayor_precios([50, 75, 46, 22, 80, 65, 8])
    assert menor == 8
    assert mayor == 80

    menor, mayor = encontrar_menor_mayor_precios([10, 20, 30, 40, 50])
    assert menor == 10
    assert mayor == 50

    menor, mayor = encontrar_menor_mayor_precios([100, 200, 150, 250])
    assert menor == 100
    assert mayor == 250

    menor, mayor = encontrar_menor_mayor_precios([5, 5, 5, 5, 5])
    assert menor == 5
    assert mayor == 5

    menor, mayor = encontrar_menor_mayor_precios([-10, 5, 50, 100, -50])
    assert menor == -50
    assert mayor == 100