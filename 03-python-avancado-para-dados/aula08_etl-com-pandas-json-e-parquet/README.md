# Aula 08 - ETL com Pandas (JSON e Parquet)

## Sobre
Projeto de ETL simples para consolidar arquivos JSON em um unico DataFrame, aplicar transformacoes basicas e gerar saidas em CSV ou Parquet. Serve como pratica de pipeline local com validacao de dados.

## Objetivos de Aprendizado
- Ler multiplos JSONs e consolidar dados com Pandas.
- Aplicar transformacoes simples no DataFrame.
- Validar estrutura e tipos com Pandera.
- Exportar resultados em CSV e Parquet.

## Estrutura do Projeto
```
.
├── data/                # JSONs de entrada
├── saidas/              # Arquivos gerados pelo pipeline
├── etl.py               # Extracao, transformacao e carga
├── schema.py            # Validacao com Pandera
├── pipeline.py          # Orquestracao e CLI
├── pyproject.toml       # Dependencias e config do Poetry
├── poetry.lock          # Lockfile do Poetry
└── README.md            # Documentacao do modulo
```

## Tecnologias e Ferramentas
- Pandas: processamento e transformacao de dados.
- Pandera: validacao de schema e tipos.
- Poetry: gerenciamento de dependencias e ambientes.

## Pre-requisitos
- Python 3.11+
- Poetry instalado
- Conhecimentos basicos de Python e Pandas

## Como Usar

### Instalacao
```bash
poetry install
```

### Execucao
Com arquivo especifico:
```bash
python pipeline.py --input data/arquivo.json --output saidas/resultado.parquet --format parquet
```

Para CSV:
```bash
python pipeline.py --input data/arquivo.json --output saidas/resultado.csv --format csv
```

Para processar todos os JSONs em `data/`:
```bash
python pipeline.py --input-dir data --output saidas/resultado.parquet --format parquet
```

## Conteudo Real
- `etl.py` carrega um ou mais JSONs com `pd.read_json`, concatena em um unico DataFrame e aplica limpeza simples em colunas e strings.
- `schema.py` cria um schema com `pandera.infer_schema` e valida o DataFrame antes de salvar.
- `pipeline.py` orquestra o fluxo, resolve os inputs (lista de arquivos ou pasta), valida e salva no formato escolhido.

## Conexoes com a Formacao
- Pre-requisitos: `03-python-avancado-para-dados/aula01` a `aula07` (fundamentos de Python e Pandas).
- Proximos passos: `03-python-avancado-para-dados/aula09` em diante (pipelines mais completos e validacao).

## Recursos Adicionais
- Pandas: https://pandas.pydata.org/docs/
- Pandera: https://pandera.readthedocs.io/
- Poetry: https://python-poetry.org/docs/

## Autor
Arthur Cardoso
