import pytest

from calculadora.operaciones import sumar, restar , multiplicar, dividir

#Casos de priueba
def test_sumar_positivos(numeros):
    a,b = numeros
    assert sumar(a,b) == 12
  
def test_multiplicar (numeros):
    a,b = numeros
    assert multiplicar(a,b) == 20

def test_dividir (numeros):
    a,b = numeros
    assert dividir(a,b) == 5
