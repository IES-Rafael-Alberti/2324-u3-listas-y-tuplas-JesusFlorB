from src.ejercicio11 import producto_escalar

def test_producto_escalar():
    assert producto_escalar([1, 2, 3], [-1, 0, 2]) == 5
    assert producto_escalar([0, 0, 0], [1, 2, 3]) == 0
    assert producto_escalar([2, 3, 4], [3, 2, 1]) == 16
    assert producto_escalar([1, 0, 0], [0, 1, 0]) == 0
    assert producto_escalar([], []) == 0