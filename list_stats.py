# ---- Funciones provistas (NO modificar) ----

def find_min(numbers):
    """Dada una lista de numeros, retorna el menor valor."""
    minimo = numbers[0]
    for num in numbers:
        if num < minimo:
            minimo = num
    return minimo


def find_max(numbers):
    """Dada una lista de numeros, retorna el mayor valor."""
    maximo = numbers[0]
    for num in numbers:
        if num > maximo:
            maximo = num
    return maximo

# ---- Funciones a implementar ----

def range_of(numbers):
    """
    Retorna la diferencia entre el maximo y el minimo de la lista.
    Debe USAR las funciones find_min y find_max.

    Ejemplo: range_of([3, 1, 7, 2]) -> 6  (7 - 1)
    """
    if numbers == []:
        return 0
    
    return find_max(numbers) - find_min(numbers)


def average(numbers):
    """
    Retorna el promedio de los numeros en la lista, redondeado a 1 decimal.
    Si la lista esta vacia, retorna 0.0.
    Usar un bucle for para sumar los elementos.

    Ejemplo: average([10, 20, 30]) -> 20.0
    """
    if numbers == []:
        return 0.0
    
    total = 0
    for num in numbers:
        total += num
    
    avg = total / len(numbers)
    return round(avg, 1)


def describe(numbers):
    """
    Retorna un string con el formato:
    "Min:{min} Max:{max} Range:{range} Avg:{avg}"

    Debe USAR las funciones find_min, find_max, range_of y average.
    Si la lista esta vacia, retorna "Empty list".

    Ejemplo: describe([3, 1, 7, 2]) -> "Min:1 Max:7 Range:6 Avg:3.2"
    """
    if numbers == []:
        return "Empty list"
    
    min_val = find_min(numbers)
    max_val = find_max(numbers)
    range_val = max_val - min_val
    avg_val = average(numbers)
    
    return f"Min:{min_val} Max:{max_val} Range:{range_val} Avg:{avg_val}"
