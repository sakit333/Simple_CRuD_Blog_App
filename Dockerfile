# Use a lightweight Python base
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy requirements if you have one (recommended)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app code
COPY . .

# Expose Streamlit’s port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "your_app_file.py", "--server.port=8501", "--server.address=0.0.0.0"]
