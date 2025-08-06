FROM python:3.11-slim

WORKDIR /app
COPY handler.py requirements.txt ./

RUN pip install -r requirements.txt

ENV RUNPOD_HANDLER=handler.handler

CMD ["python3", "handler.py"]
