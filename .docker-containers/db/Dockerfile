FROM postgres:9.6.2

# Для удобного подключения к БД создаем пользователя
RUN groupadd -r docker && useradd -r -g docker docker

# Копируем скрипт конфигурации 
RUN mkdir -p /docker-entrypoint-initdb.d
COPY configure.sh /docker-entrypoint-initdb.d/configure.sh
RUN chmod 755 /docker-entrypoint-initdb.d/configure.sh