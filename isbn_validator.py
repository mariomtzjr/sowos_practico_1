# ISBN
def isValidISBN(isbn):
    # Comprobamos la longitud del isbn
    if len(isbn) != 10:
        return False

    # Suma de los primeros 9 dígitos
    # Sumatoria de la multiplicación del valor de cada caracter en el isbn por
    # cada elemento de la "lista orden descendente del 10 al 1"
    _sum = sum([(int(isbn[i])*(10 - i)) for i in range(len(isbn)-1)])

    # Verificamos si el último elemento del isbn es una X,
    # si true, sumamos su valor (10), sino, la sumatoria es hasta el elemento 9
    _sum += 10 if isbn[9] == 'X' else int(isbn[9])
    print(_sum)

    # Retornamos true si la suma de los dígitos es divisible por 11
    return (_sum % 11 == 0)

isValidISBN('007462542X')
