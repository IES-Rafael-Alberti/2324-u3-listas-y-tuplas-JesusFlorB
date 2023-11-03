"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""

def eliminar_aprobadas(asignaturas, notas):
    #Esta funcion elimina de la lista las asignaturas aprobadas.
    asignaturas_a_repetir = []  #Lista para almacenar las asignaturas a repetir

    for i in range(len(asignaturas)):
        if notas[i] >= 5.0:  #Si la nota es mayor o igual a 5.0, se añade a la lista de asignaturas a repetir
            asignaturas_a_repetir.append(asignaturas[i])

    for asignatura in asignaturas_a_repetir:
        asignaturas.remove(asignatura)

    return asignaturas

if __name__ == "__main__":

    #Lista de asignaturas
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

    #Lista para almacenar las notas
    notas = []

    #Pedir al usuario las notas para cada asignatura
    for asignatura in asignaturas:
        nota = float(input(f"Ingrese la nota de {asignatura}: "))
        notas.append(nota)

    #Eliminar las asignaturas aprobadas
    asignaturas_restantes = eliminar_aprobadas(asignaturas, notas)

    #Mostrar las asignaturas a repetir
    if asignaturas_restantes:
        print("Debes repetir las siguientes asignaturas:")
        for asignatura in asignaturas_restantes:
            print(asignatura)
    else:
        print("Felicidades, has aprobado todas las asignaturas.")