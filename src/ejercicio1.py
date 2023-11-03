"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla."""

def listar_asignaturas(asignaturas):
    #Esta funcion toma una lista de asignaturas y las muestra por pantalla.
    for asignatura in asignaturas:
        print(asignatura)

if __name__ == "__main__":

    #Creamos una lista de asignaturas
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

    #Llamamos a la funcion para listar las asignaturas
    listar_asignaturas(asignaturas)