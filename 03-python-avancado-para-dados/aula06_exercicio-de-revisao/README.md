# Aula 06 - Fluxo de Qualidade com pre-commit

## 📋 Sobre

Aula 06 focada no fluxo de qualidade local com pre-commit. O repositório concentra configurações de lint e formatação, além de um arquivo de testes para uma função de transformação.

## 🎯 Objetivos de Aprendizado

- Configurar pre-commit para padronizar qualidade antes do commit.
- Aplicar formatação e lint com blue (baseado no black), isort e flake8.
- Praticar criação de ambiente e dependências com Poetry.

## 📁 Estrutura do Projeto

```
.
|-- .flake8
|-- .gitignore
|-- .pre-commit-config.yaml
|-- .python-version
|-- main.py
|-- poetry.lock
`-- pyproject.toml
```

## 🛠️ Tecnologias e Ferramentas

- Python 3.11: versão base do projeto.
- Poetry: gerenciamento de ambiente e dependências.
- pre-commit: execução automática de hooks antes do commit.
- black: formatador usado nos hooks (dependência do blue).
- isort: organização de imports.
- flake8: lint de estilo e qualidade.
- blue: formatador instalado via Poetry (inclui black 22.1.0 como dependência).

## 📦 Pré-requisitos

- Python 3.11 instalado.
- Poetry instalado.
- Git configurado para usar pre-commit.

## 🚀 Como Usar

### Se não tiver Poetry ou pyenv instalados

Instale o Poetry (recomendado via pipx):

```bash
python -m pip install --user pipx
python -m pipx ensurepath
pipx install poetry
```

Se quiser gerenciar versões do Python, instale o pyenv-win:
https://github.com/pyenv-win/pyenv-win

Se não usar pyenv, você pode apontar o Python direto no Poetry:

```bash
poetry env use C:\caminho\para\python.exe
```

### Instalação

```bash
poetry install
```

Se as ferramentas ainda não estiverem no projeto, instale com:

```bash
poetry add pre-commit isort flake8 blue
```

### Definir versão do Python e criar o venv

Se você usa `pyenv`, fixe a versão do projeto:

```bash
pyenv local 3.11.5
```

Crie/ative o ambiente virtual com Poetry:

```bash
poetry env use 3.11.5
poetry env activate
```

### Configurar pre-commit

Crie o arquivo `.pre-commit-config.yaml` com os hooks desejados. Exemplo usado nesta aula:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
        args: ["--markdown-linebreak-ext=md"]
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-toml
      - id: detect-private-key
      - id: check-added-large-files

  - repo: https://github.com/psf/black-pre-commit-mirror
    rev: 24.1.1
    hooks:
      - id: black
        language_version: python3.11

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
        name: isort (python)

  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
```

Depois instale o hook e rode uma vez em todo o código:

```bash
poetry run pre-commit install
poetry run pre-commit run --all-files
```

### Configurar flake8

Crie o arquivo `.flake8` na raiz do projeto com as regras:

```ini
[flake8]
max-line-length = 89
extend-ignore = E203, E701, W291
```

### Execução

```bash
poetry run pre-commit install
poetry run pre-commit run --all-files
```

## 📚 Conteúdo Real

- `.pre-commit-config.yaml` define hooks de qualidade: trailing whitespace, end-of-file, check-yaml, check-toml, detect-private-key, check-added-large-files, além de black (python3.11), isort e flake8.
- `.flake8` configura `max-line-length = 89` e ignora `E203`, `E701` e `W291`.
- `main.py` contém testes em estilo pytest para a função `transformar` (importada de `app.etl`) usando pandas; o pacote `app` não está presente neste diretório.
- `pyproject.toml` declara as dependências do projeto (blue, pre-commit e isort) e a versão mínima de Python.

## 🔗 Conexões com a Formação

- **Pré-requisitos**: fundamentos de Python, PEP 8 e Git.
- **Próximos passos**: adicionar CI para executar pre-commit e flake8 no pipeline.

## 📖 Recursos Adicionais

- https://pre-commit.com/
- https://black.readthedocs.io/
- https://pycqa.github.io/isort/
- https://flake8.pycqa.org/
- https://python-poetry.org/docs/

## 👤 Autor

Arthur Cardoso (arthurhfcardoso@gmail.com)
