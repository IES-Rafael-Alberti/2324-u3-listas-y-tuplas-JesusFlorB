"""Escribir un programa que pregunte por una muestra de números, separados por comas, 
los guarde en una lista y muestre por pantalla su media y desviación típica."""

import math

def calcular_media(muestra):
    return sum(muestra) / len(muestra)

def calcular_desviacion_tipica(muestra):
    media = calcular_media(muestra)
    varianza = sum((x - media) ** 2 for x in muestra) / len(muestra)
    desviacion_tipica = math.sqrt(varianza)
    return desviacion_tipica

if __name__ == "__main__":
    muestra = input("Ingresa una muestra de numeros, separados por comas: ")
    muestra = [float(numero) for numero in muestra.split(",")]

    media = calcular_media(muestra)
    desviacion_tipica = calcular_desviacion_tipica(muestra)

    print(f"La media de la muestra es: {media}")
    print(f"La desviacion tipica de la muestra es: {desviacion_tipica}")