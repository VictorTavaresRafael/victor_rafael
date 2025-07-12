# Desafio de Análise de Dados e Integração com AWS S3

Este projeto foi desenvolvido como parte de um desafio para um programa de bolsas. O objetivo é demonstrar habilidades em análise de dados com Python e a integração segura com serviços da AWS, seguindo as melhores práticas de segurança para o gerenciamento de credenciais.

## 📝 Descrição do Projeto

O script `analisar_fauna.py` realiza as seguintes tarefas:
1.  Carrega os dados do plantel do Zoológico de Brasília (Dezembro/2023), extraídos do SisFauna.
2.  Realiza uma limpeza inicial dos dados, focando apenas nos animais vivos.
3.  Executa três análises de dados para responder às seguintes perguntas:
    * Qual a quantidade de animais por espécie?
    * Quantos animais nasceram entre 2020 e 2023?
    * Qual a distribuição de sexo entre todos os animais?
4.  Gera 3 arquivos `.csv` com os resultados de cada análise.
5.  Faz o upload seguro desses arquivos para um bucket no Amazon S3, utilizando a biblioteca `boto3`.

## 🔐 Boas Práticas de Segurança

A principal diretriz deste desafio é a segurança no manuseio das credenciais da AWS. Para evitar a exposição de chaves de acesso no código-fonte, este projeto utiliza a biblioteca `python-dotenv` para carregar as credenciais a partir de um arquivo `.env` local, que não é versionado no Git.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Bibliotecas Principais:**
    * `pandas`: Para manipulação e análise dos dados.
    * `boto3`: Para interagir com a API da AWS (especificamente o S3).
    * `python-dotenv`: Para gerenciar variáveis de ambiente e proteger as credenciais.

## ⚙️ Configuração e Execução

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### **Pré-requisitos**

* Python 3.8 ou superior
* Uma conta na AWS com credenciais de acesso (Chave de Acesso e Chave Secreta)
* Um bucket no S3 já criado

### **1. Clone o Repositório**
```bash
git clone [https://github.com/VictorTavaresRafael/victor_rafael](https://github.com/VictorTavaresRafael/victor_rafael)
cd NOME_DO_REPOSITORIO
```

### **2. Instale as Dependências**
Crie um ambiente virtual (recomendado) e instale as bibliotecas listadas no `requirements.txt`.
```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente (Windows)
.\venv\Scripts\activate
# Ative o ambiente (Linux/macOS)
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### **3. Configure as Variáveis de Ambiente**
Crie um arquivo chamado `.env` na raiz do projeto e preencha com suas informações:
```ini
# .env
AWS_ACCESS_KEY_ID="SUA_CHAVE_DE_ACESSO_AQUI"
AWS_SECRET_ACCESS_KEY="SUA_CHAVE_SECRETA_AQUI"
AWS_S3_BUCKET="NOME_DO_SEU_BUCKET_NO_S3"
```
**Importante:** O arquivo `.env` está listado no `.gitignore` e não deve ser enviado para o repositório.

### **4. Execute o Script**
Com tudo configurado, execute o script principal:
```bash
python analisar_fauna.py
```
O script irá imprimir os resultados das análises no terminal e, ao final, fará o upload dos arquivos `analise_especies.csv`, `analise_nascimentos_2020_2023.csv` e `analise_distribuicao_sexo.csv` para o seu bucket no S3.

## 📂 Estrutura do Projeto
```
desafio/
├── .gitignore         # Ignora arquivos sensíveis como .env
├── .env               # Arquivo local com as credenciais 
├── requirements.txt   # Lista de dependências Python
├── README.md          # Documentação do projeto
├── analisar_fauna.py  # Script principal
└── dados/
    └── sisfauna-dezembro-2023.csv # Dataset original
```