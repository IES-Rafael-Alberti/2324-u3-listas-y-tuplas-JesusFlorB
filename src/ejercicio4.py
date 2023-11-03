"""Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor."""

def ingresar_numeros():
    #Esta funcion pide al usuario que ingrese los numeros ganadores y los almacena en una lista.
    numeros = input("Ingresa los numeros ganadores separados por espacios o comas: ")
    numeros = numeros.replace(",", " ")
    numeros = numeros.split()
    return [int(numero) for numero in numeros]

def ordenar_numeros(numeros):
    #Esta funcion ordena los numeros de menor a mayor.
    return sorted(numeros)

if __name__ == "__main__":
    
    #Pedir al usuario que ingrese los numeros ganadores.
    numeros_ganadores = ingresar_numeros()

    #Ordenar los numeros
    numeros_ordenados = ordenar_numeros(numeros_ganadores)

    #Mostrar los numeros ordenados.
    print("Numeros ganadores ordenados:")
    for numero in numeros_ordenados:
        print(numero)