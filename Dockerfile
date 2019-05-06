
FROM python:3.7.3-alpine3.9

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

EXPOSE 3000

CMD ["server.py"]