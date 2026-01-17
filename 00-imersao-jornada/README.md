# 🚀 Projeto Jornada de Dados - Imersão Completa

## 📋 Sobre o Projeto

Este é o **projeto prático da Imersão Jornada de Dados**, uma experiência 4 dias onde eu construí um projeto real de dados, do zero à decisão com IA.

**Em 4 dias, eu aprendi:**
- **Dia 1:** SQL & analytics
- **Dia 2:** Python & ingestão de dados
- **Dia 3:** DBT para transformação de dados
- **Dia 4:** n8n e agente de IA
---

## 🎯 O Projeto

Uma empresa de e-commerce está abrindo sua operação digital e precisa usar dados para tomar decisões melhores. Você vai construir um sistema completo de dados que:

- ✅ Analisa vendas e clientes
- ✅ Compara preços com o mercado
- ✅ Gera insights inteligentes
- ✅ Toma decisões baseadas em dados

**Não é um exercício. É um projeto de mercado.**

---

## 📚 As 4 Aulas da Imersão

### 📊 Dia 1: SQL & Analytics
**Objetivo:** Entender o negócio com SQL

- Descobrir os produtos mais vendidos
- Identificar os principais clientes
- Comparar preços com o mercado
- Criar segmentações de clientes
n8n & automacao
**O que eu aprendi:** Pensar como analista de dados usando SQL.

---

## 📚 Material de Apoio

- **[Aula 1 - SQL & Analytics](./aulas/aula01-sql/README.md)**          - Guia completo do primeiro dia
- **[Aula 2 - Python & Ingestão](./aulas/aula02-python/README.md)**     - Lista completa de KPIs e perguntas
- **[Aula 3 - dbt & camada analitica](./aulas/aula03-dbt/README.md)**   - Documentação detalhada
- **[Aula 4 - n8n & automacao](./aulas/aula04-n8n/README.md)**          - 21 exemplos SQL com explicações

---

**Material:** [Aula 1 - SQL & Analytics](./aulas/aula01-sql/)

---

### 🐍 Dia 2: Python & Ingestão de Dados
**Objetivo:** Dados não nascem prontos

- Dados vêm de sistemas diferentes
- Formatos diferentes
- Regras diferentes

**Entrega do dia:** Um dataset unificado e confiável.

**Material:** [Aula 2 - Python & Ingestão](./aulas/aula02-python/)

---

### ⚙️ Dia 3: Engenharia de Dados
**Objetivo:** Transformar scripts em produto

- Arquitetura de dados
- Modelagem analítica
- Pipelines e orquestração

**Frase-chave:** Dados bons precisam escalar.

**Material:** [Aula 3 - Engenharia de Dados](./aulas/aula03-dbt/)

---

### 🤖 Dia 4: Inteligência Artificial
**Objetivo:** Dados tomando decisões

- IA interpretando dados
- Comparação automática de preços
- Alertas inteligentes

**Exemplo:** "Esse produto está mais caro que o mercado."

**Material:** [Aula 4 - Inteligência Artificial](./aulas/aula04-n8n/)

---

## 🎲 Os 4 Datasets do Projeto

Este projeto usou **4 datasets sintéticos** gerados com Faker para simular dados reais de e-commerce:

- **`produtos.csv`** - 200 produtos do catálogo
- **`clientes.csv`** - 50 clientes cadastrados
- **`vendas.csv`** - ~3.000 vendas (últimos 30 dias)
- **`preco_competidores.csv`** - ~680 preços de concorrentes

**Características:**
- Dados realistas (não aleatórios)
- Distribuições não-normais (como dados reais)
- Relacionamentos entre tabelas
- Problemas de integridade para prática (produtos não vendidos, vendas não cadastradas)

---

### Passo 2: Começar a Aula 1

Instruções completas em: **[Aula 1 - SQL & Analytics](./aulas/aula01-sql/README.md)**

**Resumo rápido:**
1. Importei os CSVs em um banco SQL (SQLite ou PostgreSQL)
2. Executei os 21 exemplos SQL em ordem
3. Pratiquei com os exercícios
4. Respondi perguntas de negócio

---

## 📊 Estrutura dos Datasets

### produtos.csv
```
id_produto, nome_produto, categoria, marca, preco_atual, data_criacao
```

**Exemplos de produtos:**
- Smartphone Galaxy A54
- Panela de Pressão
- Tênis Nike Air Max
- TV LED 50 Polegadas

**Total:** 200 produtos

---

### clientes.csv
```
id_cliente, nome_cliente, estado, pais, data_cadastro
```

**Nota:** A segmentação de clientes (VIP, TOP_TIER, REGULAR) foi criada usando CASE WHEN baseado no comportamento de compra (receita total). Isso fez parte do aprendizado do Dia 1!

**Total:** 50 clientes

---

### vendas.csv
```
id_venda, data_venda, id_cliente, id_produto, canal_venda, quantidade, preco_unitario
```

**Cálculo importante:**
- Receita da venda = `quantidade × preco_unitario`

**Total:** ~3.000 vendas (últimos 30 dias)

---

### preco_competidores.csv
```
id_produto, nome_concorrente, preco_concorrente, data_coleta
```

**Concorrentes monitorados:**
- Mercado Livre
- Amazon
- Magalu
- Shopee

**Total:** ~680 registros (1 coleta por produto/concorrente)

---

## 🗄️ Esquema das Tabelas Principais

### 📦 produtos (Produtos)

| Coluna | Tipo | Descrição | Exemplo |
|--------|------|-----------|---------|
| `id_produto` | TEXT (PK) | ID único do produto | `prd_20d170bd9bf7` |
| `nome_produto` | TEXT | Nome do produto | `Smartphone Galaxy A54` |
| `categoria` | TEXT | Categoria do produto | `Eletrônicos`, `Casa`, `Cozinha` |
| `marca` | TEXT | Marca do produto | `Sony`, `Samsung`, `Apple` |
| `preco_atual` | REAL | Preço atual (R$) | `73.99` |
| `data_criacao` | TEXT | Data de criação (ISO) | `2022-03-19 15:57:18` |

**Total de registros:** 200 produtos

---

### 👥 clientes (Clientes)

| Coluna | Tipo | Descrição | Exemplo |
|--------|------|-----------|---------|
| `id_cliente` | TEXT (PK) | ID único do cliente | `cus_c6a2c1df9a70` |
| `nome_cliente` | TEXT | Nome completo do cliente | `João Gabriel da Paz` |
| `estado` | TEXT | Estado (UF) | `SP`, `RJ`, `MG` |
| `pais` | TEXT | País | `Brasil` |
| `data_cadastro` | TEXT | Data de cadastro (ISO) | `2024-02-17 10:57:18` |

**Total de registros:** 50 clientes

**Nota:** A segmentação de clientes (VIP, TOP_TIER, REGULAR) foi criada usando CASE WHEN baseado no comportamento de compra. Veja o exercício `aulas/aula01-sql/exercicios/exercicio-case-when-clientes.sql` para saber como eu criei essa segmentação.

---

### 💰 vendas (Vendas)

| Coluna | Tipo | Descrição | Exemplo |
|--------|------|-----------|---------|
| `id_venda` | TEXT (PK) | ID único da venda | `sal_f2414a3f34b6` |
| `data_venda` | TEXT | Data e hora da venda (ISO) | `2025-12-13 13:15:07` |
| `id_cliente` | TEXT (FK) | ID do cliente | `cus_63ade3c52c55` |
| `id_produto` | TEXT (FK) | ID do produto | `prd_91f3a368678f` |
| `canal_venda` | TEXT | Canal de venda | `ecommerce`, `loja_fisica` |
| `quantidade` | INTEGER | Quantidade vendida | `1`, `2`, `3` |
| `preco_unitario` | REAL | Preço unitário da venda (R$) | `116.99` |

**Total de registros:** ~3.000 vendas (últimos 30 dias)

**Relacionamentos:**
- `id_cliente` → `clientes.id_cliente`
- `id_produto` → `produtos.id_produto`

**Cálculo importante:**
- Receita da venda = `quantidade × preco_unitario`

---

### 🏪 preco_competidores (Preços de Concorrentes)

| Coluna | Tipo | Descrição | Exemplo |
|--------|------|-----------|---------|
| `id_produto` | TEXT (FK) | ID do produto | `prd_20d170bd9bf7` |
| `nome_concorrente` | TEXT | Nome do concorrente | `Mercado Livre`, `Amazon`, `Magalu`, `Shopee` |
| `preco_concorrente` | REAL | Preço do concorrente (R$) | `72.51` |
| `data_coleta` | TEXT | Data da coleta (ISO) | `2026-01-08 14:38:10` |

**Total de registros:** ~680 registros

**Relacionamentos:**
- `id_produto` → `produtos.id_produto`

**Concorrentes:**
- Mercado Livre
- Amazon
- Magalu
- Shopee

**Característica especial:**
- Cada combinação `id_produto + nome_concorrente` é única (1 coleta por produto/concorrente)

---

## 🔗 Diagrama de Relacionamentos

```
┌─────────────┐
│  clientes   │
│             │
│ id_cliente  │◄─────┐
│    ...      │      │
└─────────────┘      │
                     │
┌─────────────┐      │      ┌─────────────┐
│  produtos   │      │      │   vendas    │
│             │      │      │             │
│ id_produto  │◄─────┼──────┤ id_cliente  │
│    ...      │      │      │ id_produto  │
└─────────────┘      │      │    ...      │
      │              │      └─────────────┘
      │              │
      │              │
      ▼              │
┌─────────────────┐  │
│preco_competidores│ │
│                 │  │
│   id_produto    │──┘
│ nome_concorrente│
│    ...          │
└─────────────────┘
```

---

## 🎯 Perguntas de Negócio que respondi

Este projeto foi criado para responder perguntas reais de negócio usando dados. Abaixo estão todas as perguntas que podemos responder:

### 📊 Análise de Produtos

1. **Quais produtos temos no catálogo?**
2. **Quais são os produtos mais caros?**
3. **Quais produtos nunca foram vendidos?**
4. **Quais são os produtos mais vendidos?**
5. **Qual é a distribuição de produtos por categoria?**

### 💰 Análise de Vendas

6. **Qual é o total de vendas e receita?**
7. **Qual é a distribuição de receita por canal de venda?**
8. **Quais são as vendas por período?**
9. **Quais vendas foram feitas de produtos não cadastrados?**

### 👥 Análise de Clientes

10. **Quem são nossos clientes?** (criar segmentação usando CASE WHEN)
11. **Quais clientes compram mais?**
12. **Quais clientes nunca compraram?**

### 🏪 Análise Competitiva

13. **Quais produtos estão mais caros que os concorrentes?**
14. **Quais produtos estão mais baratos no concorrente?**
15. **Qual é a diferença percentual entre nossos preços e dos concorrentes?**
16. **Quais produtos top sellers estão mais caros que todos os concorrentes?**

### 📈 Análises Avançadas

17. **Qual é a receita total por categoria?**
18. **Quais categorias geram mais de R$ 50.000 em receita?**
19. **Qual é o ticket médio por segmento de cliente?**
20. **Quais produtos têm preço acima da média geral?**
21. **Quais produtos estão mais caros que a média dos concorrentes?**

---

## 📚 Estrutura do Projeto

```
00-imersao-jornada/
├── data/                          # CSVs gerados
│   ├── produtos.csv
│   ├── clientes.csv
│   ├── vendas.csv
│   └── preco_competidores.csv
├── aulas/
│   ├── aula01-sql/                # Dia 1: SQL & Analytics
│   │   ├── queries/               # 21 exemplos SQL
│   │   ├── exercicios/            # Exercícios práticos
│   │   ├── README.md              # Guia completo do Dia 1
│   │   ├── KPIS.md                # KPIs e perguntas de negócio
│   │   └── ESTRUTURA_DADOS.md     # Documentação dos datasets
│   ├── aula02-python/             # Dia 2: Python & Ingestão
│   │   ├── exemplos/              # 4 exemplos Sde ETL/ELT
│   │   ├── README.md              # Guia completo do Dia 2
│   │   └── requirements.txt       # Dependências para manipulação de dados
│   ├── aula03-dbt/                # Dia 3: dbt & camada analitica
│   │   ├── dbt_project.yml        # configuracao do projeto dbt
│   │   ├── profiles.yml           # perfil de conexao
│   │   ├── README.md              # guia completo do dia 3
│   │   ├── requirements.txt       # dependencias do dia 3
│   │   └── models/                # modelos dbt por camada
│   │       ├── _sources.yml       # definicao das fontes raw
│   │       ├── bronze/            # camada bronze (dados brutos padronizados)
│   │       ├── silver/            # camada silver (dados limpos/enriquecidos)
│   │       └── gold/              # camada gold (KPIs e data marts)
│   ├── aula04-n8n/                # Dia 4: n8n & automacao
│   │   ├── GUIA_INSTALACAO.md     # guia de instalacao do n8n
│   │   ├── README.md              # guia completo do dia 4
│   │   └── workflows/             # fluxos n8n prontos para importar
└── README.md                      # Este arquivo
```

---

## 🎲 Características dos Dados

### Distribuições Realistas (Não-Normais)

- **Produtos:** 30 produtos "top sellers" vendem muito mais
- **Clientes:** Todos os clientes têm peso igual na geração (segmentação foi criada com CASE WHEN)
- **Preços:** Distribuídos em buckets (R$ 29,90 a R$ 1.499,90)
- **Quantidades:** Maioria compra 1 unidade (72%), poucos compram mais
- **Horários:** Picos em manhã (8-12h) e tarde (15-19h)
- **Canais:** 72% ecommerce, 28% loja física
- **Promoções:** 55% sem desconto, 45% com desconto (5% a 15%)
- **Concorrentes:** Nem todos têm preço para todos os produtos (85% de cobertura)
- **Tênis:** Produtos de tênis são os menos vendidos e têm preço o dobro dos concorrentes

---

## 🔧 Seed e Reproducibilidade

O script usa `SEED = 42` para garantir que os dados gerados sejam sempre os mesmos (reproducibilidade).

Para gerar dados diferentes, altere o `SEED` ou remova a linha `random.seed(SEED)`.

---

## 📝 Notas Técnicas

- **Encoding:** UTF-8
- **Separador:** Vírgula (CSV padrão)
- **Datas:** Formato ISO (YYYY-MM-DD HH:MM:SS)
- **Preços:** 2 casas decimais (R$)
- **IDs:** UUIDs curtos (prefixo + 12 caracteres hex)
- **Nomes de produtos:** Produtos brasileiros reais (ex: "Smartphone Galaxy A54", "Panela de Pressão")

---

## ✅ Validação

Após gerar, o script imprimiu um resumo:

```
✅ CSVs gerados com sucesso:
- data/produtos.csv           (products=200 | top_sellers=30)
- data/clientes.csv            (customers=50)
- data/vendas.csv              (sales=3000 | ~100/dia por 30 dias)
- data/preco_competidores.csv  (rows=680 | competitors=4)
```

**Nota:** A segmentação de clientes foi criada usando CASE WHEN baseado no comportamento de compra.

---

## 🎯 Resultado Final da Imersão

Ao final dos 4 dias, eu realizei:

✅ **Projeto real no GitHub**  
✅ **SQL aplicado a negócio**  
✅ **Pipeline de dados funcionando**  
✅ **n8n com IA interpretando dados e gerando insights**  

**Isso é o que o mercado procura.**

---

## 💡 Frase de Ouro

> **"Eu não estou aprendendo ferramentas. Estou aprendendo como dados resolvem problemas reais."**

Cada query, cada script, cada pipeline que construí responde uma pergunta de negócio. Sempre me questiono: **"Por que isso importa?"**

---

**Uma grande jornada! 🚀**
