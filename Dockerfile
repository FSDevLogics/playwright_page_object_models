# Imagem oficial da Microsoft atualizada para a versão 1.62.0
FROM mcr.microsoft.com/playwright/python:v1.62.0-jammy

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Instala o gerenciador de pacotes 'uv'
RUN pip install uv

# Copia todos os arquivos do seu projeto para dentro do container
COPY . .

# Usa o uv para sincronizar as dependências do projeto
RUN uv sync

# Comando que será executado automaticamente quando o container ligar
CMD ["uv", "run", "pytest"]