FROM python:3.10-slim

ENV TZ=America/Sao_Paulo

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
RUN opentelemetry-bootstrap -a install

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]