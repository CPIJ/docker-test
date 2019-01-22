FROM python:3.7.2-alpine

ADD ./src /api

WORKDIR /api

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]

