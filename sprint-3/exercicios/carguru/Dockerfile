# Usar uma imagem base oficial do Python
FROM python:3.9-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar o script para o diretório de trabalho
COPY carguru.py .

# Comando para executar o script quando o container iniciar
CMD ["python", "carguru.py"]