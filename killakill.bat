@echo off
FOR /F "tokens=5" %%T IN ('netstat -ano ^| findstr :5000') DO (
    taskkill /PID %%T /F 2>nul
)

FOR /F "tokens=5" %%T IN ('netstat -ano ^| findstr :4200') DO (
    taskkill /PID %%T /F 2>nul
)

echo Les processus utilisant les ports 5000 et 4200 ont été tués.
pause
