# a_calculadora
Executa cálculos matemáticos simples (+, - , x e /)

## Pré-requisitos
- Python >= 3.10
- `venv` + `pip`

## Arranque rápido
```powershell
cd a-calculadora
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -e .

a-calculadora --help
a-calculadora somar 2 3
```
Para correr os testes, ver secção [Desenvolvimento e testes](#desenvolvimento-e-testes).

## venv/pip
python -m venv .venv && .venv\Scripts\Activate.ps1
pip install -U pip && pip install -e .
Copy-Item .env.example .env
a-calculadora --help

## Configuração
| Variável | Descrição | Defeito | Exemplo |
| `APP_ENV` | Ambiente de execução | `dev` | `prod` |
| `LOG_LEVEL` | Nível de logging | `INFO` | `DEBUG` |

## Utilização
CLI
a-calculadora somar 2 3

## Estrutura
a_calculadora/
    src/a_calculadora/
        __init__.py
        cli.py
        scritp.py
    .env
    .env.example
    .gitignore
    pyproject.toml
    README.md

## Desenvolvimento e testes
Com o ambiente virtual ativo, instala também as ferramentas de desenvolvimento:

```powershell
python -m pip install -e ".[dev]" # Instalar o projeto com as ferramentas de desenvolvimento

python -m pytest -q OU python -m pytest -v # Testes; com -v mostra os nomes
python -m black . # Formatação
python -m ruff check . # Erros e más práticas
```

a-calculadora --help
a-calculadora somar 2 3
a-calculadora subtrair 5 -3
a-calculadora dividir 10 4
a-calculadora dividir 10 0
echo $LASTEXITCODE
a-calculadora --log-level DEBUG multiplicar 6 7

## Licença e contacto
Licença <tipo>. Contacto: <marianapsr@hotmail.com>.
