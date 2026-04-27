FROM python:3.10-slim



WORKDIR /app



COPY requirements.txt .

COPY . .



RUN pip install --no-cache-dir streamlit pandas scikit-learn fastapi uvicorn



CMD ["streamlit", "run", "app.py"]