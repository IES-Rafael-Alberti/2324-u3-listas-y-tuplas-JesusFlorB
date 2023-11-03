from src.ejercicio3 import mostrar_notas

def test_mostrar_notas(capsys):
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    notas = [8.5, 7.2, 9.0, 6.8, 8.3]
    
    mostrar_notas(asignaturas, notas)
    captured = capsys.readouterr()
    assert captured.out == "En Matemáticas has sacado 8.5.\nEn Física has sacado 7.2.\nEn Química has sacado 9.0.\nEn Historia has sacado 6.8.\nEn Lengua has sacado 8.3.\n"