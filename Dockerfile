FROM python:3.7.3-stretch

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./config.json . 
COPY src /src

EXPOSE 4458

WORKDIR "./src"

CMD ["python", "src/app.py"]