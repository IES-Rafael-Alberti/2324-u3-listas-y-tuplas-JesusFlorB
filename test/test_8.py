from src.ejercicio8 import es_palindromo

def test_es_palindromo():
    assert es_palindromo("reconocer") == True
    assert es_palindromo("python") == False
    assert es_palindromo("radar") == True
    assert es_palindromo("cívico") == False
    assert es_palindromo("oso") == True
    assert es_palindromo("programa") == False
    assert es_palindromo("") == True