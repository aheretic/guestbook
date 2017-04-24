psql --username "$POSTGRES_USER" -c "CREATE DATABASE $DB_NAME"
psql --username "$POSTGRES_USER" -c "CREATE USER $DB_USER WITH password '$DB_USER_PASSWORD'"
psql --username "$POSTGRES_USER" -d "$DB_NAME" -c "create schema authorization $DB_SCHEMA"

echo "# General settings" >> /var/lib/postgresql/data/postgresql.conf
echo "default_transaction_isolation = 'read committed'" >> /var/lib/postgresql/data/postgresql.conf
echo "timezone = 'UTC'" >> /var/lib/postgresql/data/postgresql.conf
echo "client_encoding = 'UTF8'" >> /var/lib/postgresql/data/postgresql.conf

echo "# Performance tuning by http://pgtune.leopard.in.ua" >> /var/lib/postgresql/data/postgresql.conf
echo "max_connections = $POSTGRES_CONFIG_MAX_CONNECTIONS" >> /var/lib/postgresql/data/postgresql.conf
echo "shared_buffers = $POSTGRES_CONFIG_SHARED_BUFFERS" >> /var/lib/postgresql/data/postgresql.conf
echo "effective_cache_size = $POSTGRES_CONFIG_EFFECTIVE_CACHE_SIZE" >> /var/lib/postgresql/data/postgresql.conf
echo "work_mem = $POSTGRES_CONFIG_WORK_MEM" >> /var/lib/postgresql/data/postgresql.conf
echo "maintenance_work_mem = $POSTGRES_CONFIG_MAINTENANCE_WORK_MEM" >> /var/lib/postgresql/data/postgresql.conf
echo "checkpoint_segments = $POSTGRES_CONFIG_CHECKPOINT_SEGMENTS" >> /var/lib/postgresql/data/postgresql.conf
echo "checkpoint_completion_target = $POSTGRES_CONFIG_CHECKPOINT_COMPLETION_TARGET" >> /var/lib/postgresql/data/postgresql.conf
echo "wal_buffers = $POSTGRES_CONFIG_WAL_BUFFERS" >> /var/lib/postgresql/data/postgresql.conf
echo "default_statistics_target = $POSTGRES_CONFIG_DEFAULT_STATISTICS_TARGET" >> /var/lib/postgresql/data/postgresql.conf