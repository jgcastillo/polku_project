FROM python:3.13.5-bullseye

# 1. --- Configuración del Entorno y Zona Horaria ---
# Establecemos las variables de entorno al principio.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ=America/Caracas

# 2. --- Instalación de Dependencias del Sistema ---
RUN apt-get update \
    && apt-get install -y tzdata \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && apt-get install -y netcat-openbsd postgresql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 3. --- Configuración del Directorio de Trabajo y Dependencias de Python ---
WORKDIR /usr/src/app

# Se crea un entorno virtual para aislar las dependencias de la aplicación.
RUN python -m venv /opt/venv
# Se asegura que el venv esté en el PATH para que los comandos lo usen.
ENV PATH="/opt/venv/bin:$PATH"

# Se copian e instalan los requerimientos de Python.
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. --- Copia del Código Fuente y Permisos ---
# Se copia el código de la aplicación al contenedor.
COPY ./polku_backend ./polku_backend

# Se crea un usuario no-root para ejecutar la aplicación por seguridad.
RUN adduser --system --group nonroot
USER nonroot

