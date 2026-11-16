# CLI (com argparse)

# Imports
from __future__ import annotations

import argparse
import logging
import os
import sys

from a_calculadora import script

logger = logging.getLogger(__name__)
""" Autor das mensagens de log deste ficheiro.
    O logger é usado para mensagens de erro, debug, etc. (não para stdout).
"""

OPERACOES = {
    "somar": script.somar,
    "subtrair": script.subtrair,
    "multiplicar": script.multiplicar,
    "dividir": script.dividir
}

# Função que define a CLI
def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="a-calculadora", description="Calculadora simples (+, -, x, /).")
    p.add_argument("--log-level", default=os.getenv("LOG_LEVEL", "INFO"), help="Nível de log (DEBUG, INFO, WARNING, ERROR).")
    sub = p.add_subparsers(dest="cmd", required=True) # Prepara o espaço para os subcomandos
    
    for operacao in OPERACOES:
        sp = sub.add_parser(operacao, help=f"Calcula: {operacao} dois números.")
        sp.add_argument("a", type=float, help="primeiro número")
        sp.add_argument("b", type=float, help="segundo número")

    return p

# Função que executa o main (a CLI)
def main(argv: list[str] | None = None) -> int:
    """ Executa a CLI:
            argv: por defeito é None, e nesse caso o argparse lê o que foi escrito no terminal;
            -> int: indica que a função devolve um número, que será o código de saída;
            args: guarda tudo (args.cmd, args.log_level, args.formato, args.dest);
            logging: escreve em stderr por defeito;
    """

    args = _build_parser().parse_args(argv)

    logging.basicConfig(level=args.log_level.upper(), format="%(asctime)s %(levelname)s %(name)s: %(message)s")

    try:
        if args.cmd in OPERACOES:
            resultado = OPERACOES[args.cmd](args.a, args.b)
            logger.debug("%s(%s, %s) = %s", args.cmd, args.a, args.b, resultado)
            print(resultado)  # stdout: só o resultado
            return 0
    except ZeroDivisionError as exc:
            logger.error("%s", exc)  # stderr
            return 2  # valores inválidos
    
    except Exception as exc: # em produção, tipificar erros
        logger.exception("Falha ao executar comando: %s", exc)
        return 1

if __name__ == "__main__":
    """ sys.exit(...) termina o programa com o número 0 ou 1 como código de saída,
        que é o que depois aparece em $LASTEXITCODE.
    """
    sys.exit(main())