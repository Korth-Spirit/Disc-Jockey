FROM python:3-windowsservercore
WORKDIR /app

COPY requirements.txt aw64.dll /app/
RUN pip install -r requirements.txt
COPY greeter/ /app/disc_jockey

ENTRYPOINT [ "python /app/disc_jockey" ]