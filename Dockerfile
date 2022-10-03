FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
COPY .env /app/.env
ENV FLASK_DEBUG=0
CMD ["gunicorn", "--bind", ":8080", "--workers", "2", "app:app"]