# ========== Base Image ==========
FROM python:3.10-slim

# ========== Set Working Directory ==========
WORKDIR /app

# ========== Install system dependencies ==========
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# ========== Copy requirements ==========
COPY requirements.txt .

# ========== Install Python dependencies ==========
RUN pip install --no-cache-dir -r requirements.txt

# ========== Copy application files ==========
COPY . .

# ========== Expose Streamlit default port ==========
EXPOSE 8501

# ========== Run the app ==========
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
