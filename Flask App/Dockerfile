# Use an official Python runtime as a parent image
FROM jupyter/scipy-notebook

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install additional packages
RUN pip install joblib

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
