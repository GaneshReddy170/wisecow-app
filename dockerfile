# Use a base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install required Python packages
RUN pip install -r requirements.txt

# Expose the port Wisecow runs on
EXPOSE 4499

# Start the app
CMD ["python", "app.py"]
