# frontend/Dockerfile
FROM python:3.11

# Establece el directorio de trabajo
WORKDIR /app

# Copia el código fuente
COPY ./src /app
COPY requirements.txt .

# Instala las dependencias
RUN apt-get update && \
    apt-get install -y libgtk-3-0 libnss3 libasound2 libatk-adaptor libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 libxkbcommon0 libxshmfence1 libxext6 libxfixes3 libxi6 libxtst6 libglib2.0-0
RUN apt-get update && \
    apt-get install -y \
    libgstreamer1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    libgstreamer-plugins-good1.0-dev \
    libgstreamer-plugins-bad1.0-dev \
    libgstreamer-plugins-ugly1.0-dev \
    gstreamer1.0-libav \
    gstreamer1.0-tools \
    gstreamer1.0-x \
    gstreamer1.0-alsa \
    gstreamer1.0-gl \
    gstreamer1.0-gtk3 \
    gstreamer1.0-pulseaudio

RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto si aplica (Flet puede usar 8550 por defecto)
EXPOSE 8550

# Comando para ejecutar la app
CMD ["python", "main.py"]