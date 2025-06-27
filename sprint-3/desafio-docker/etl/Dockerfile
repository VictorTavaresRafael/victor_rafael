# Usa uma imagem oficial do Python como base. 'slim' é uma versão mais leve.
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o script etl.py da sua máquina local para o diretório /app dentro do container
COPY etl.py .

# Instala as dependências necessárias (neste caso, apenas pandas)
# O comando RUN é executado durante a construção da imagem
RUN pip install pandas

# Define o comando que será executado quando o container iniciar
CMD ["python", "etl.py"]