.PHONY: help start-mlflow start-services start-prefect-agent run-flow run-all other-target

# Configuration
CONFIG := $(shell type config.json)
MLFLOW_HOST := $(shell echo $(CONFIG) | jq -r .mlflow.host)
MLFLOW_PORT := $(shell echo $(CONFIG) | jq -r .mlflow.port)
BACKEND_URI := $(shell echo $(CONFIG) | jq -r .mlflow.backend_uri)
ARTIFACT_LOCATION := $(shell echo $(CONFIG) | jq -r .mlflow.artifact_location)

## help: Show this help message
help: Makefile
	@sed -n 's/^##//p' $<

## start-mlflow: Start the MLflow server
start-mlflow:
	@echo "Starting MLflow..."
	powershell -Command "Start-Process -NoNewWindow mlflow -ArgumentList 'server --host $(MLFLOW_HOST) --port $(MLFLOW_PORT) --backend-store-uri $(BACKEND_URI) --default-artifact-root $(ARTIFACT_LOCATION)'"

start-services:
	@echo "Starting Prefect Server..."
	powershell -Command "Start-Process -NoNewWindow -ArgumentList 'server start' -FilePath 'prefect'"

start-prefect-agent:
	@echo "Starting Prefect Agent..."
	powershell -Command "Start-Process -NoNewWindow -ArgumentList 'agent local start' -FilePath 'prefect'"

run-flow:
	python workflow_mgmt/runner.py

run-all: start-mlflow start-services
	@echo "Executing runner.py..."
	make run-flow

## other-target: Description for the other target
other-target:
	@echo "Other target actions here..."
