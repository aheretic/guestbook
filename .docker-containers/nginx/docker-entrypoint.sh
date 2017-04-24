#!/bin/bash
set -e

ln -sf /etc/nginx/nginx.conf.$PROJECT_ENVIRONMENT /etc/nginx/nginx.conf 

exec "$@"