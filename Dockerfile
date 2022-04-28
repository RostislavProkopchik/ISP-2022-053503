FROM python:3.8-alpine3.14

WORKDIR /app

COPY . .

CMD ["python", "lab1.py"]
