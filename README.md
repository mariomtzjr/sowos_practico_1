# Examen 1

## factorial.py
La función factorial devuelve el factorial de un número. Para ejecutarlo desde el IDLE de python, sólo es necesario abrir el archivo, modificar el valor (n) que recibe la función factorial(n) y ejecutar el script (F5).

Para ejecutar el archivo desde línea de comandos, es necesario ejecutar el siguiente comando:  
`python factorial.py numero`  
Donde número debe ser un número natural positivo.

## polygonArea.py
La función polygonArea devuelve el área de un polígono. Para ejecutar el archivo desde el IDLE de Python, se realiza el mismo procedimiento que para el archivo *factorial.py*, y para ejecutarlo desde línea de comandos, es necesario ejecutar el siguiente comando:  
`python polygonArea.py n_lados`  
Donde n_lados es un número natural positivo.  

## isbn_validator.py
La función isValidISBN devuelve true si cumple con el comportamiento descrito por el Pseudocódigo. Para ejecutar el archivo desde el IDLE de Python, se realiza el mismo procedimiento que para el archivo *factorial.py* y *polygonArea.py*, y para ejecutarlo desde línea de comandos, es necesario ejecutar el siguiente comando:  
`python isbn_validator.py isbn`    
Donde isbn es una cadena isbn.  

## Pseudocódigo para validar ISBN

1. Partimos de una cadena que representa el ISBN.
2. Comprobamos que la longitud isbn = 10
2. Declaramos una lista = [10,9,8,7,6,5,4,3,2,1]
3. Realizamos la sumatoria de la múltiplicación del valor de cada caracter en el isbn por cada elemento de la lista
4. Verificamos si el último elemento del isbn es una X, si es así, sumamos su valor (10), de lo contrario la sumatoria es sólo hasta el caracter 9.
5. suma % 11 = 0 ?, entonces el isbn es válido
