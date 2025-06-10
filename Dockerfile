FROM python:3.13.3-alpine3.20

## Install system dependencies and update certificates
RUN apk update && apk upgrade --no-cache && \
    apk add --no-cache chromium-chromedriver ca-certificates && \
    update-ca-certificates && \
    rm -rf /var/cache/apk/*

# Create directory for project name (ensure it does not conflict with default debian /opt/ directories).
RUN mkdir -p /opt/app
WORKDIR /opt/app

## Install other requirements
COPY requirements.txt .
RUN pip3 install  --upgrade pip \
    && pip3 install -r requirements.txt

## Copy resources
COPY . .

# Set display port and dbus env to avoid hanging
ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

# Run tests and indicate success or failure
RUN set -e; \
    python -m unittest discover -s tests -v; \
    echo "\n\n====================\nAll tests passed!\n====================\n"
