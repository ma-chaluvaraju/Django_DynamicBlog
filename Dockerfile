# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to avoid Python output buffering and keep it consistent
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file first for better caching
COPY requirements.txt /app/

# Install any dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the application files into the container
COPY . /app/

# Expose the port the app will run on
EXPOSE 8000

# Run Django migrations and start the server (adjust if needed for production)
CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
