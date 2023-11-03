"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura, 
y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista 
y <nota> cada una de las correspondientes notas introducidas por el usuario."""

def ingresar_notas(asignaturas):
    #Esta funcion pide al usuario las notas para cada asignatura.
    notas = []
    for asignatura in asignaturas:
        nota = float(input(f"Ingrese la nota de {asignatura}: "))
        notas.append(nota)
    return notas

def mostrar_notas(asignaturas, notas):
    #Esta funcion muestra las asignaturas y sus respectivas notas.
    for i in range(len(asignaturas)):
        print(f"En {asignaturas[i]} has sacado {notas[i]}.")

if __name__ == "__main__":
    
    #Lista de asignaturas
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

    #Pedir al usuario las notas
    notas = ingresar_notas(asignaturas)

    #Mostrar las asignaturas y notas
    mostrar_notas(asignaturas, notas)