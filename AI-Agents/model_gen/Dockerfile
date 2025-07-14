FROM python:3.10-slim

RUN apt-get update && apt-get install -y git && \
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 && \
    pip install transformers trimesh

WORKDIR /app
COPY generate_model.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "generate_model.py", "A spiral vase"]
