from src.ejercicio13 import (calcular_desviacion_tipica, calcular_media)
import math

def test_calcular_media():
    muestra = [1, 2, 3, 4, 5]
    assert calcular_media(muestra) == 3.0

def test_calcular_desviacion_tipica():
    muestra = [1, 2, 3, 4, 5]
    assert math.isclose(calcular_desviacion_tipica(muestra), 1.4142135623730951)
