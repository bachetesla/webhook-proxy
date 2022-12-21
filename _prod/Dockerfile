FROM python:latest

WORKDIR /code

COPY . .

RUN pip install -U pip && pip install -r requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port 8080", "--workers 5"]