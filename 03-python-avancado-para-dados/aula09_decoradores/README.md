# Aula 09 - Decoradores

## 📋 Sobre
Exemplos praticos de decoradores aplicados a logging, com uso de loguru e scripts simples para exercitar chamadas de funcao e configuracao de logs.

## 🎯 Objetivos de Aprendizado
- Entender o conceito de decoradores e como encapsular comportamento em funcoes.
- Aplicar logging com loguru, incluindo niveis e escrita em arquivo.
- Esbocar um fluxo de ETL com CLI simples e passos de transformacao.

## 📁 Estrutura do Projeto
```
.
|-- data/
|-- pics/
|-- .python-version
|-- etl.py
|-- exemplo_00.py
|-- logging_exemplo_erros.py
|-- pipeline.py
|-- pyproject.toml
|-- README.md
|-- log_2026-01-20_11-32-55_057978.log
|-- log_2026-01-20_11-34-39_869521.log
|-- meu_arquivo_de_logs.log
|-- meu_arquivo_de_logs_critial.log
|-- terminal-da-aula00.log
|-- terminal-da-aula01.log
|-- utils_log.py
`-- __init__.py
```

## 🛠️ Tecnologias e Ferramentas
- Python: execucao dos scripts.
- loguru: logging simplificado com configuracao de arquivos.
- pandas: carga e transformacao no esqueleto de ETL.

## 📦 Pre-requisitos
- Python 3.12+
- Poetry
- pandas instalado (usado em `etl.py`, nao declarado no `pyproject.toml`).

## 🚀 Como Usar
### Instalacao
```bash
poetry install
```

### Execucao
```bash
poetry run python exemplo_00.py
poetry run python logging_exemplo_erros.py
```
```bash
poetry run python pipeline.py -i data/arquivo.json -o saidas/resultado.parquet -f parquet
```

## 📚 Conteudo
- `utils_log.py`: define um decorator de log com loguru e grava logs em arquivo.
- `exemplo_00.py`: aplica o decorator em uma funcao simples para demonstrar logs.
- `logging_exemplo_erros.py`: exemplos de niveis de log (debug a critical).
- `etl.py`: funcoes de carga, transformacao e escrita usando pandas.
- `pipeline.py`: CLI de ETL; depende de um modulo `schema.py` (nao presente no diretorio) e das funcoes em `etl.py`.

### Resumo do Terminal
- Geracao do `pyproject.toml` com `poetry init` e dependencia `loguru`, com faixa de Python `>=3.12,<4.0`.
- Tentativa de adicionar configuracao de dependencia como comando do shell (erro `command not found`), corrigido ao editar o `pyproject.toml`.
- `poetry show` falhou sem `poetry.lock`, resolvido com `poetry install`.
- Instalacao do projeto falhou por nao haver pacote; resolvido com `poetry install --no-root`.
- Execucao com `python run exemplo_00.py` falhou (arquivo `run` inexistente); corrigido para `poetry run python exemplo_00.py`.
- `exemplo_00.py` apresentou `SyntaxError` por bloco `try` incompleto; ajustado e reexecutado com logs emitidos.
- Gravacao de terminal via `script` falhou no Git Bash; gravacao passou a usar `exec > >(tee -a terminal-da-aula01.log) 2>&1`.

## 🔗 Conexoes com a Formacao
- **Pre-requisitos**: fundamentos de funcoes, logs e boas praticas em Python.
- **Proximos passos**: aplicar decoradores em pipelines e monitoramento de execucao.

## 📖 Recursos Adicionais
- https://loguru.readthedocs.io/
- https://docs.python.org/3/library/functools.html

## 👤 Autor
arthurhfcardoso
