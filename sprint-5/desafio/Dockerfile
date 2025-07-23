# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de dependências para o diretório de trabalho
COPY requirements.txt ./

# Instale as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie o script de ingestão e o arquivo de dados para o diretório de trabalho
COPY ingestao_raw_camada.py ./
COPY data/series.csv ./

# Comando que será executado quando o container iniciar
CMD ["python", "ingestao_raw_camada.py"]