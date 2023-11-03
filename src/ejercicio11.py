"""Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar."""

def producto_escalar(vector1, vector2):
    #Esta funcion calcula el producto escalar de dos vectores.
    return sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

if __name__ == "__main__":

    vector1 = [1, 2, 3]
    vector2 = [-1, 0, 2]

    resultado = producto_escalar(vector1, vector2)

    print(f"El producto escalar de los vectores {vector1} y {vector2} es: {resultado}")