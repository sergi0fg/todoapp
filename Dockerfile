# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de tu código
COPY . .

# Expone el puerto en el que tu aplicación escuchará
EXPOSE 5000

# Comando para ejecutar tu aplicación
CMD ["python", "app.py"]  # Asegúrate de que este sea el comando correcto para tu app
