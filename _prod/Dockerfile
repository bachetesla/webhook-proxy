FROM python:latest

WORKDIR /code

COPY . .

RUN pip install -U pip && pip install -r requirments.txt

CMD ["python", "main.py"]