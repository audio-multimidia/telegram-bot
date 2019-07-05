FROM python:3.7.3-stretch

RUN apt update && apt install -y ffmpeg 

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY src /src

COPY config.json .
COPY serviceAccount.json .

EXPOSE 4458

CMD ["python", "src/app.py"]