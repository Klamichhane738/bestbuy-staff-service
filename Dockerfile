# Use the official Python image as the base image
FROM python:3.10-slim

# Set environment variables to adhere to the 12-factor principles
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the Flask app will run on
EXPOSE 8000

# Command to run the application
CMD ["python", "app.py"]
