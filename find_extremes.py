# Replace the "ANSWER HERE" for your answer

def find_min(numbers):
    """
    Dada una lista de numeros (no vacia), retorna el menor valor.
    Usar un bucle for para recorrer la lista.

    Ejemplo: find_min([3, 1, 7, 2]) -> 1
    Ejemplo: find_min([5, 5, 5]) -> 5
    Ejemplo: find_min([-3, -1, -7]) -> -7
    """
    minimo = numbers[0]
    
    for num in numbers:
        if num < minimo:
            minimo = num
    
    return minimo


def find_max(numbers):
    """
    Dada una lista de numeros (no vacia), retorna el mayor valor.
    Usar un bucle for para recorrer la lista.

    Ejemplo: find_max([3, 1, 7, 2]) -> 7
    Ejemplo: find_max([5, 5, 5]) -> 5
    Ejemplo: find_max([-3, -1, -7]) -> -1
    """
    maximo = numbers[0]
    
    for num in numbers:
        if num > maximo:
            maximo = num
    
    return maximo


def count_negatives(numbers):
    """
    Dada una lista de numeros, retorna la cantidad de numeros negativos.
    Si la lista esta vacia, retorna 0.

    Ejemplo: count_negatives([3, -1, -7, 2]) -> 2
    Ejemplo: count_negatives([1, 2, 3]) -> 0
    Ejemplo: count_negatives([-1, -2, -3]) -> 3
    """
    contar_negativos = 0
    
    for num in numbers:
        if num < 0:
            contar_negativos += 1
    
    return contar_negativos
