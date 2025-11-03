FROM python:3.10-slim
COPY requirements.txt .
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
