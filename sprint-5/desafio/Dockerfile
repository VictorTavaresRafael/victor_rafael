# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de dependências
COPY requirements.txt ./

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie APENAS o script de ingestão
COPY ingestao_raw_camada.py ./

# Cria um diretório para os dados que virão do volume
RUN mkdir data

# Comando que será executado quando o container iniciar
CMD ["python", "ingestao_raw_camada.py"]