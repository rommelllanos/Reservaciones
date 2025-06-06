@echo off
REM ------------------------------------------------------------
REM run_reserva.bat
REM Este script abre una ventana de consola y ejecuta:
REM    python ReservaPuestos.py
REM Asegúrate de que:
REM   • python.exe esté en tu PATH, o pon la ruta completa a python.exe
REM   • ReservaPuestos.py esté en la carpeta correcta
REM ------------------------------------------------------------

REM 1) Cambia al directorio donde está el script
cd /d "C:\Users\romme\Downloads\Reservaciones_Project\Reservaciones_Project v2"

REM 2) Ejecuta el script
python ReservaPuestos.py

REM 3) Espera unos segundos antes de cerrar
timeout /t 10 /nobreak > nul
