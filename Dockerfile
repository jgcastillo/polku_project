
FROM python:3.13-slim as builder

# Establece el directorio de trabajo
WORKDIR /usr/src/app

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala dependencias de sistema necesarias SOLO para construir paquetes
RUN apt-get update \
  && apt-get -y install gcc \
  && apt-get clean

# Instala las dependencias de Python en un entorno virtual
# Esto aísla las dependencias y facilita su copia a la siguiente etapa
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copia e instala los requerimientos
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt