from src.ejercicio1 import listar_asignaturas

def test_listar_asignaturas(capsys):
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
    listar_asignaturas(asignaturas)
    captured = capsys.readouterr()
    assert captured.out == "Matematicas\nFisica\nQuimica\nHistoria\nLengua\n"