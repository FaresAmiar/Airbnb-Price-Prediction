@echo off
mlflow server --host %1 --port %2 --backend-store-uri %3 --default-artifact-root %4
