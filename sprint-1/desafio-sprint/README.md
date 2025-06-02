# Desafio Sprint — Normalização e Modelagem Dimensional

## 📌 Objetivo

O objetivo do desafio foi **normalizar uma base de dados de locações** (forma desnormalizada em uma única tabela) e posteriormente **converter esse modelo relacional em um modelo dimensional**, utilizando o esquema estrela. A entrega envolve a explicação do processo, criação das estruturas em SQL e o desenho do modelo.

---

## 🧠 Etapas Executadas

### 1. Análise da Base de Dados

A tabela original `tb_locacao` incluía informações mistas:
- Dados do cliente
- Informações do carro (incluindo combustível)
- Dados do vendedor
- Detalhes da locação

Essa estrutura era redundante e apresentava diversas **anomalias**.

---

### 2. Normalização (até 3FN)

Criamos tabelas separadas, garantindo:
- Remoção de redundâncias
- Independência entre entidades
- Relacionamentos bem definidos por chaves estrangeiras

Tabelas criadas:
- `Cliente`
- `Carro`
- `Combustivel`
- `Vendedor`
- `Locacao`

📄 Script: [`Modelo Normalizado`](./modelo_normalizado.sql)

---

### 3. Modelagem Dimensional (Esquema Estrela)

Para fins analíticos, criamos um modelo dimensional com uma **tabela fato** (`FatoLocacao`) e diversas **dimensões**:
- `DimCliente`
- `DimCarro`
- `DimCombustivel`
- `DimVendedor`
- `DimTempo`

📄 Script: [`Modelo Dimensional`](./modelo_dimensional.sql)

---

### 4. Diagramas

Utilizamos o padrão **PlantUML** para gerar os diagramas:

- Diagrama ER do modelo relacional
- Diagrama Estrela do modelo dimensional

Estão disponíveis:
- [`Modelo Normalizado`](./diagramas/diagrama-modelo-relacional-normalizado.png) 
- [`Modelo Dimensional`](./diagramas/diagrama-modelo-dimensional.png)
  
---

## 🧪 Execução e Evidências

Durante o processo:
- Utilizamos o SQLite para inspecionar os dados originais e entender os relacionamentos
- Criamos os scripts SQL com as estruturas normalizadas e dimensionais
- Utilizamos [`PlantUML`](https://www.plantuml.com/plantuml) para modelagem visual
- Testamos todos os scripts em ambiente PostgreSQL via pgAdmin
---

## 📂 Organização do Repositório

```bash

📂 desafio-sprint
├── modelo_normalizado.sql
├── modelo_dimensional.sql
├── README.md
├── diagramas/
│   ├── diagrama-modelo-relacional-normalizado.png
│   ├── diagrama-modelo-dimensional.png
│   ├── codigo_diagrama_normalizado.puml
│   └── codigo_diagrama_dimensional.puml
└── evidencias/
    ├── 00_execucao_modelo_base.png
    ├── 01_tabelas_criadas_normalizado.png
    ├── 02_tabelas_criadas_dimensional.png
    ├── 03_insercao_dados_teste.png
    ├── 04_visualizacao_dados.png
    ├── 05_criacao_diagrama_normalizado.png
    └── 06_criacao_diagrama_dimensional.png
