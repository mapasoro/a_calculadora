# Testar a lógica do script.py

import pytest

from a_calculadora import script


def test_somar():
    assert script.somar(2, 3) == 5


def test_subtrair():
    assert script.subtrair(5, 3) == 2


def test_multiplicar():
    assert script.multiplicar(6, 7) == 42


def test_dividir():
    assert script.dividir(10, 4) == 2.5


def test_dividir_por_zero():
    with pytest.raises(ZeroDivisionError):
        script.dividir(10, 0)