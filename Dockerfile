FROM python:3.8-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./workflow_mgmt /app/workflow_mgmt
COPY ./data/AB_NYC_2019.csv /app/data/AB_NYC_2019.csv
#COPY ./infrastructure /app/infrastructure

RUN pip install --no-cache-dir -r requirements.txt



CMD ["python", "./workflow_mgmt/runner.py"]
