FROM python:3.9

WORKDIR /app

COPY r.txt .

RUN pip install --no-cache-dir -r r.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]