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

- Diagrama ER do modelo relacional
- Diagrama Estrela do modelo dimensional

Estão disponíveis:
- [`Modelo Normalizado`](./diagramas/diagrama-modelo-relacional-normalizado.png) 
- [`Modelo Dimensional`](./diagramas/diagrama-modelo-dimensional.png)
  
---

## 🧪 Execução e Evidências

Durante o processo:
- Utilizamos o SQLite para inspecionar e entender os dados
- Criamos os scripts SQL com as estruturas normalizadas e dimensionais
---

## 📂 Organização do Repositório

```bash
📁 desafio-sprint
├── modelo_normalizado.sql
├── modelo_dimensional.sql
├── README.md
└── diagramas/
    ├── diagrama_er.png
    └── esquema_estrela.png
