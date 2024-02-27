FROM python:3.8  
#O la versión que uses

# Instalar cron
RUN apt-get update && apt-get -y install cron

# Copiar el script y el archivo cron al contenedor
COPY . /app/
COPY cron /etc/cron.d/cron

# Dar permisos de ejecución
RUN chmod 0644 /etc/cron.d/cron
RUN touch /var/log/cron.log
WORKDIR /app
RUN pip install -r requirements.txt
# RUN pip install -e .

# Ejecutar el comando cron en el arranque
CMD cron && tail -f /var/log/cron.log