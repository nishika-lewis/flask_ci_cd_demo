# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy everything from local folder to container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Tell Cloud Run which port to expose
EXPOSE 8080

# Command to run the app
CMD ["python", "app.py"]
