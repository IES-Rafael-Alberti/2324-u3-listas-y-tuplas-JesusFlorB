from src.ejercicio7 import filtrar_abecedario

def test_filtrar_abecedario():
    abecedario = list("abcdefghijklmnopqrstuvwxyz")
    resultado = filtrar_abecedario(abecedario)
    assert resultado == ['a', 'b', 'd', 'e', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 's', 't', 'v', 'w', 'y', 'z']
