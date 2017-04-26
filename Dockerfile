FROM python:2.7

RUN groupadd -r docker && useradd -r -g docker docker

# Updating sources.list for contrib and non-free
RUN echo "deb http://httpredir.debian.org/debian jessie main contrib non-free" > /etc/apt/sources.list; \
    echo "deb http://httpredir.debian.org/debian jessie-updates main contrib non-free" >> /etc/apt/sources.list; \
    echo "deb http://security.debian.org jessie/updates main contrib non-free" >> /etc/apt/sources.list

# Application packages
RUN apt-get update && apt-get install -y \
    libmemcached-dev \
    libpcre3 \
    libpcre3-dev \
    postgresql-client \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

COPY docker-entrypoint.sh /
RUN chmod 755 /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

RUN mkdir -p /app

WORKDIR /app
RUN pip install --upgrade pip==9.0.1

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app
RUN chown -R docker:docker /app

WORKDIR /app

CMD ["python"]