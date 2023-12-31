# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables to prevent buffering and writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Set environment variable to not buffer stdout and stderr
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/
