from src.ejercicio9 import contar_vocales

def test_contar_vocales():
    resultado = contar_vocales("Murcielago")
    assert resultado == {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}

    resultado = contar_vocales("Programa")
    assert resultado == {'a': 2, 'e': 0, 'i': 0, 'o': 1, 'u': 0, 'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}

    resultado = contar_vocales("aeiouAEIOU")
    assert resultado == {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1}

    resultado = contar_vocales("")
    assert resultado == {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}