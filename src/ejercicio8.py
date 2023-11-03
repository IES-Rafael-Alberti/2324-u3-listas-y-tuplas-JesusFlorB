"""Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo."""

def es_palindromo(palabra):
    #Esta funcion verifica si una palabra es un palíndromo.
    palabra = palabra.lower()  #Convertimos la palabra a minusculas
    return palabra == palabra[::-1]

if __name__ == "__main__":

    palabra = input("Ingresa una palabra: ")

    if es_palindromo(palabra):
        print(f"{palabra} es un palindromo.")
    else:
        print(f"{palabra} no es un palindromo.")