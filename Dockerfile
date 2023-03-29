FROM python:3.9

WORKDIR /FastAPI

COPY ./requirements.txt /FastAPI/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /FastAPI/requirements.txt

COPY . .

CMD ["uvicorn", "main:APIapp", "--host", "0.0.0.0", "--port", "80"]