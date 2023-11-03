from src.ejercicio6 import eliminar_aprobadas

def test_eliminar_aprobadas():
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
    notas = [6.0, 7.5, 4.0, 8.2, 5.5]
    
    resultado = eliminar_aprobadas(asignaturas, notas)
    
    assert resultado == ["Quimica"]