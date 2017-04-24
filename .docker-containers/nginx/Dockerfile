FROM nginx:1.9
MAINTAINER Andrew Timonin <andrew@impsite.com>

# Создаем пользователя
RUN groupadd -r docker && useradd -r -g docker docker

# Настраиваем конфигурацию nginx
RUN rm /etc/nginx/nginx.conf
COPY conf/ /etc/nginx/

COPY docker-entrypoint.sh /
RUN chmod 755 /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

WORKDIR /app

CMD ["nginx", "-g", "daemon off;"]
