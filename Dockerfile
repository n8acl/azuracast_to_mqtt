FROM python:latest

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --break-system-packages

COPY . .

CMD ./azuracast-mqtt.py