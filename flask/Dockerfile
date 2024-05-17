# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the application files into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port on which your Flask application will run
EXPOSE 5000

# Define the command to run your Flask application
CMD ["python", "app.py"]
