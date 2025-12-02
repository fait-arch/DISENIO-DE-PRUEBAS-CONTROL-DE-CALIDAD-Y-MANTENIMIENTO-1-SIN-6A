FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY src/ ./src/
COPY locust/ ./locust/
COPY start.sh ./

# Make the start script executable
RUN chmod +x start.sh

# Command to run when starting the container
CMD ["./start.sh"]