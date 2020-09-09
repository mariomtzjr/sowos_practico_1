"""
    1 -> 1 4
    2 -> 5 8
    3 -> 13 12
    4 -> 25 16
    5 -> 41 20
    6 -> 61
    n^2 + (n-1)^2
"""
import sys

numero = sys.argv[1]

def polygonArea(numero):
    return (numero**2 + (numero - 1)**2)
