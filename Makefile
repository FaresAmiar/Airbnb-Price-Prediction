.PHONY: help start-mlflow start-services start-prefect-agent run-flow run-all other-target

# Configuration
MLFLOW_HOST := $(shell jq -r ".mlflow.local.host" config.json)
MLFLOW_PORT := $(shell jq -r '.mlflow.local.port' config.json)
BACKEND_URI := $(shell jq -r .mlflow.local.backend_uri config.json)
ARTIFACT_LOCATION := $(shell  jq -r .mlflow.local.artifact_location config.json)

$(info MLFLOW_HOST is $(MLFLOW_HOST))
$(info MLFLOW_PORT is $(MLFLOW_PORT))
$(info BACKEND_URI is $(BACKEND_URI))
$(info ARTIFACT_LOCATION is $(ARTIFACT_LOCATION))


ifeq ($(OS),Windows_NT)
    DETECTED_OS := WINDOWS
else
    UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Linux)
        DETECTED_OS := UNIX
    endif
    ifeq ($(UNAME_S),Darwin)
        DETECTED_OS := MAC
    endif
endif

help: Makefile
	@sed -n 's/^##//p' $<

start-mlflow:
	@echo "Starting MLflow on $(DETECTED_OS)..."
ifeq ($(DETECTED_OS),WINDOWS)
	powershell -Command "Start-Process -NoNewWindow mlflow -ArgumentList 'server --host $(MLFLOW_HOST) --port $(MLFLOW_PORT) --backend-store-uri $(BACKEND_URI) --default-artifact-root $(ARTIFACT_LOCATION)'"
else
	mlflow server --host $(MLFLOW_HOST) --port $(MLFLOW_PORT) --backend-store-uri $(BACKEND_URI) --default-artifact-root $(ARTIFACT_LOCATION) &
endif

start-services:
	@echo "Starting Prefect Server on $(DETECTED_OS)..."
ifeq ($(DETECTED_OS),WINDOWS)
	powershell -Command "Start-Process -NoNewWindow -ArgumentList 'server start' -FilePath 'prefect'"
else
	prefect server start &
endif

start-prefect-agent:
	@echo "Starting Prefect Agent on $(DETECTED_OS)..."
ifeq ($(DETECTED_OS),WINDOWS)
	powershell -Command "Start-Process -NoNewWindow -ArgumentList 'agent local start' -FilePath 'prefect'"
else
	prefect agent local start &
endif

run-flow:
	python workflow_mgmt/runner.py

run-all: start-mlflow start-services
	@echo "Executing runner.py..."
	make run-flow

print:
	@echo $(MLFLOW_PORT)

other-target:
	@echo "Other target actions here..."
