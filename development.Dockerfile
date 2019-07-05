FROM python:3.7.3-stretch

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY src /src

EXPOSE 4458

RUN apt update && \
    apt install -y curl ffmpeg && \
    curl -sL https://deb.nodesource.com/setup_4.x | bash && \
    apt-get install nodejs && \
    npm install -g nodemon

WORKDIR "./src"

CMD ["nodemon", "--exec", "python", "src/app.py"]