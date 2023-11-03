"""Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal."""

def contar_vocales(palabra):
    #Esta funcion cuenta el numero de veces que aparece cada vocal en una palabra.
    vocales = "aeiouAEIOU"
    contador_vocales = {vocal: 0 for vocal in vocales}  #Inicializamos un contador para cada vocal

    for letra in palabra:
        if letra in contador_vocales:
            contador_vocales[letra] += 1

    return contador_vocales

if __name__ == "__main__":

    palabra = input("Ingresa una palabra: ")

    resultado = contar_vocales(palabra)

    for vocal, contador in resultado.items():
        print(f"La vocal {vocal} aparece {contador} veces en la palabra.")