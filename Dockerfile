# Use an official Python runtime as a parent image
FROM python:3.8-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD start.py /app

# Install any needed packages specified in requirements.txt
RUN pip3 install psycopg2-binary

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python3", "start.py"]