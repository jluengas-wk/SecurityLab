FROM python:3.9-slim-bookworm AS builder

ENV PIP_NO_CACHE_DIR=1
WORKDIR /src

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY app-vulnerable/backend/requirements.txt ./
RUN pip install --upgrade pip \
    && pip wheel --wheel-dir /wheels -r requirements.txt

# -----------------------------------------------------------------------------

FROM python:3.9-slim-bookworm

RUN useradd --create-home --home-dir /app --shell /usr/sbin/nologin opc

WORKDIR /app

COPY --from=builder /wheels /wheels
COPY app-vulnerable/backend/requirements.txt /app/requirements.txt

# Instalacion desde los wheels ya resueltos 
RUN pip install --no-cache-dir --no-index --find-links /wheels -r requirements.txt \
    && rm -rf /wheels

# El proceso corre como usuario sin privilegios
COPY --chown=opc:opc app-vulnerable/backend /app

RUN mkdir -p /app/data && chown opc:opc /app/data

USER opc

EXPOSE 5000

CMD ["python", "app.py"]