"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista."""

def mostrar_asignaturas(asignaturas):
    #Esta funcion muestra un mensaje para cada asignatura en la lista.
    for asignatura in asignaturas:
        print(f"Yo estudio {asignatura}.")

if __name__ == "__main__":

    #Lista de asignaturas
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

    #Mostrar asignaturas
    mostrar_asignaturas(asignaturas)