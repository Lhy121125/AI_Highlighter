# this is existing CUDA-enabled image as a base
FROM alvarobartt/torch-gpu:py310-cu12.3-torch-2.2.0


WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
