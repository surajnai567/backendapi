#!/usr/bin/env bash
set -e
echo "***** Gidai Docker Entrypoint *****"

if [[ -z "${CONTAINER_START_COMMAND}" ]]; then
    echo "Missing env variable CONTAINER_START_COMMAND"
    exit 10
fi
if [[ -z "${DJANGO_API_PORT}" ]]; then
    echo "Missing env variable DJANGO_API_PORT"
    exit 15
fi

# Start Flask Server
echo "Received CONTAINER_START_COMMAND: $CONTAINER_START_COMMAND"
case "$CONTAINER_START_COMMAND" in
    gunicorn)
        # Apply db migrations
        echo "Migrating db changes"
        python manage.py makemigrations
        python manage.py migrate
        # Prepare log files and start outputting logs to stdout
        touch /srv/logs/gunicorn.log
        touch /srv/logs/access.log
        tail -n 0 -f /srv/logs/*.log &

        echo "Starting gunicorn server"
        GUNICORN_WORKERS=${GUNICORN_WORKERS:-3}
        GUNICORN_THREADS=${GUNICORN_THREADS:-3}
        echo "Using config GUNICORN_WORKERS=$GUNICORN_WORKERS, GUNICORN_THREADS=$GUNICORN_THREADS"
        exec gunicorn gshop_backend.wsgi \
            --name gidai_django \
            --bind 0.0.0.0:${DJANGO_API_PORT} \
            --workers=${GUNICORN_WORKERS} \
            --threads=${GUNICORN_THREADS} \
            --log-level=info \
            "$@"
        ;;
    dev)
        # Apply db migrations
        echo "Migrating db changes"
        python manage.py makemigrations
        python manage.py migrate

        echo "Starting dev web server (non-production use only)"
        python manage.py runserver 0.0.0.0:${DJANGO_API_PORT}
        ;;
    disabled)
        echo "Disable container execution (troubleshooting)"
        tail -f /dev/null
        ;;
    *)
        echo "Invalid startup command"
        exit 1
        ;;
esac