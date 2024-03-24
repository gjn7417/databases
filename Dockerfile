# Use an official Python runtime as a parent image
FROM python:3.12-bookworm

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Use Poetry to install dependencies
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Set Flask run configuration
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080
ENV FLASK_ENV=development

# Make port 5001 available to the world outside this container
EXPOSE 8080

# Run wsgi.py when the container launches
CMD ["python", "wsgi.py"]