# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /backend

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . /backend/

# Expose the port that the FastAPI application runs on
EXPOSE 8090

# Define the command to run the FastAPI application when the container starts
CMD ["python","run.py"]
