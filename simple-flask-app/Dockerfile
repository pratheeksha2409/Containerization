# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory
WORKDIR /usr/src/app

# Copy requirements.txt to the working directory
COPY requirements.txt ./

# Install app dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app source code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Start the app
CMD ["python", "./app.py"]

