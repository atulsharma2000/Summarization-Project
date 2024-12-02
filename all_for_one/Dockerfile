# Use the official Python image from the Docker Hub
FROM python:3.9

# Set environment variables for Selenium (if needed)
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary system packages for Selenium (e.g., Firefox)
RUN apt-get update && \
    apt-get install -y \
    wget \
    unzip \
    firefox-esr \
    && rm -rf /var/lib/apt/lists/*

# Install geckodriver for Firefox (Selenium)
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz && \
    tar -xvzf geckodriver-v0.30.0-linux64.tar.gz && \
    mv geckodriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/geckodriver && \
    rm geckodriver-v0.30.0-linux64.tar.gz

# Set the working directory in the container
WORKDIR /app

# Copy requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application:
CMD ["python", "app.py"]