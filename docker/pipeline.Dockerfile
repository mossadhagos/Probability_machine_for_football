FROM python:3.12-slim

WORKDIR /app

COPY requirements/pipeline.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY pipline/ ./pipeline/
COPY shared/ ./shared/
COPY db/ ./db/
COPY data/ ./data/

CMD ["python", "-m", "pipeline.main"]