# Operações da calculadora

def somar(a: float, b: float) -> float:
    """ Soma dois números. """
    return a + b

def subtrair(a: float, b: float) -> float:
    """ Subtrai dois números. """
    return a - b

def multiplicar(a: float, b: float) -> float:
    """ Multiplica dois números. """
    return a * b

def dividir(a: float, b: float) -> float:
    """ Divide dois números. """
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b
