# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    resultado = []
    for row in matrix:
        for valor in row:
            resultado.append(valor)
    
    return resultado


def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    resultado = []
    for row in matrix:
        total = 0
        for valor in row:
            total += valor
        resultado.append(total)
    
    return resultado


def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    if matrix == []:
        return []
    
    num_cols = len(matrix[0])
    resultado = []
    
    for col in range(num_cols):
        total = 0
        for row in matrix:
            total += row[col]
        resultado.append(total)
    
    return resultado
