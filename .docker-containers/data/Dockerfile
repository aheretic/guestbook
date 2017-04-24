FROM debian:jessie
MAINTAINER Andrew Timonin <andrew@impsite.com>

# Создаем пользователя
RUN groupadd -r docker && useradd -r -g docker docker

# Создаем необходимые директории с нужными правами
RUN mkdir -p /app/media ; chown -R docker:docker /app/media
RUN mkdir -p /app/static ; chown -R docker:docker /app/static
RUN mkdir -p /app/tmp ; chown -R docker:docker /app/tmp

# Добавляем VOLUME
VOLUME ["/app/media"]
VOLUME ["/app/static"]
VOLUME ["/app/tmp"]
VOLUME ["/var/lib/postgresql/data"]

# Logs dir
RUN mkdir -p /app/logs ; chown -R docker:docker /app/logs
VOLUME ["/app/logs"]

CMD ["true"]
