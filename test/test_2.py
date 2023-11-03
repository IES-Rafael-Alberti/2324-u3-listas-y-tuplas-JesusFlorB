from src.ejercicio2 import mostrar_asignaturas

def test_mostrar_asignaturas(capsys):
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
    mostrar_asignaturas(asignaturas)
    captured = capsys.readouterr()
    assert captured.out == "Yo estudio Matematicas.\nYo estudio Fisica.\nYo estudio Quimica.\nYo estudio Historia.\nYo estudio Lengua.\n"