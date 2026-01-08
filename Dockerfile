FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libffi-dev \
        libssl-dev \
        libxml2-dev \
        libxslt1-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY webscraper/ /app/

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["scrapy"]
CMD ["crawl", "quotes", "-O", "/data/items.json"]
