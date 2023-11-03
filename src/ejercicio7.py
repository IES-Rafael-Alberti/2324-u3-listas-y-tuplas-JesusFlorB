"""Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
y muestre por pantalla la lista resultante."""

def filtrar_abecedario(abecedario):
    #Esta funcion elimina las letras que ocupan posiciones múltiplos de 3.
    return [letra for i, letra in enumerate(abecedario, start=1) if i % 3 != 0]

if __name__ == "__main__":

    #Lista con el abecedario
    abecedario = list("abcdefghijklmnopqrstuvwxyz")

    #Llamamos a la funcion para filtrar el abecedario
    abecedario_filtrado = filtrar_abecedario(abecedario)

    #Mostramos la lista resultante
    print(abecedario_filtrado)