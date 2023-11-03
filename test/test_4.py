from src.ejercicio4 import (ingresar_numeros, ordenar_numeros)

def test_ingresar_numeros(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5 2 8 12 1')
    assert ingresar_numeros() == [5, 2, 8, 12, 1]

def test_ordenar_numeros():
    assert ordenar_numeros([5, 2, 8, 12, 1]) == [1, 2, 5, 8, 12]
