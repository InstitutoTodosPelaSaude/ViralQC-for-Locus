FROM mambaorg/micromamba:1.5.1

USER root

ENV TZ=America/Sao_Paulo
ENV PATH="/opt/conda/bin:$PATH"

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y unzip && apt-get clean
RUN micromamba install -y -n base \
    -c conda-forge \
    -c bioconda \
      snakemake-minimal=7.32.4 \
      blast=2.16.0 \
      nextclade=3.15.0 \
      seqtk=1.5 \
      ncbi-datasets-cli=18.9.0 \
      taxonkit=0.20.0 \
      pip && \
    micromamba clean -ay

RUN pip install -r requirements.txt

EXPOSE 8000

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
RUN opentelemetry-bootstrap -a install

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]