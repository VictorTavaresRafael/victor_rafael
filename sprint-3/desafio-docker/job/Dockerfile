# Usa a mesma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o script job.py para dentro do container
COPY job.py .

# Instala as dependências: pandas para manipulação de dados,
# matplotlib e seaborn para os gráficos.
RUN pip install pandas matplotlib seaborn

# Define o comando padrão para iniciar o container
CMD ["python", "job.py"]