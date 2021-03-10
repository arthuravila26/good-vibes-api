FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 80
CMD ["python3", "run.py"]