# Testar a CLI (cli.py)

import pytest

from a_calculadora.cli import main


def test_somar_sucesso(capsys):
    codigo = main(["somar", "2", "3"])
    saida = capsys.readouterr()

    assert codigo == 0
    assert saida.out.strip() == "5.0"


def test_subtrair_com_negativo(capsys):
    codigo = main(["subtrair", "5", "-3"])

    assert codigo == 0
    assert capsys.readouterr().out.strip() == "8.0"


def test_dividir_por_zero(capsys, caplog):
    codigo = main(["dividir", "10", "0"])

    assert codigo == 2
    assert capsys.readouterr().out == ""        # nada em stdout
    assert "dividir por zero" in caplog.text    # erro registado no log


def test_argumento_invalido():
    with pytest.raises(SystemExit) as excinfo:
        main(["somar", "2", "abc"])

    assert excinfo.value.code == 2