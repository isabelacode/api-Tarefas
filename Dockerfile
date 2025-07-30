FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/

# Create a script to wait for postgres and run migrations
COPY docker-entrypoint.sh /code/
RUN chmod +x /code/docker-entrypoint.sh

# Expose port
EXPOSE 8000

# Run the application
CMD ["./docker-entrypoint.sh"]
