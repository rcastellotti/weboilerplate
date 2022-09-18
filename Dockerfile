FROM python:3.9

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]