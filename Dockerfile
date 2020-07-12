# Application Base image
FROM python:3.6-slim

# the working directory where the application would be started
WORKDIR /todo

# Copy requirements file to install app requirements
COPY requirements.txt .

# Update packages and install requirements
RUN apt-get update && \
    apt-get install bash && \
    pip install -r requirements.txt && \
    pip install gunicorn

# Copy application files to the working directory
COPY . .

# Expose port for app accessibilty
ENV PORT 5000
EXPOSE $PORT

# Command to start the application
CMD ["/bin/bash", "-c", "source .env ; gunicorn --bind 0.0.0:$PORT --workers 2  app:app"]
