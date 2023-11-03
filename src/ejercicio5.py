"""Escribir un programa que almacene en una lista los números del 1 al 10 
y los muestre por pantalla en orden inverso separados por comas."""

def mostrar_numeros_invertidos():
    #Creamos una lista con números del 1 al 10
    numeros = list(range(1, 11))

    #Invertimos el orden de la lista
    numeros_invertidos = numeros[::-1]

    #Convertimos los numeros a cadenas y los unimos con comas
    numeros_como_cadenas = [str(numero) for numero in numeros_invertidos]
    resultado = ', '.join(numeros_como_cadenas)

    #Mostramos el resultado por pantalla
    return(resultado)

if __name__ == "__main__":

    print(mostrar_numeros_invertidos())