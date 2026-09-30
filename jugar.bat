@echo off
setlocal
set "PYTHON=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"

if not exist "%PYTHON%" (
  echo No se encontro Python 3.12 en:
  echo %PYTHON%
  echo Instala Python 3.12 y vuelve a intentarlo.
  pause
  exit /b 1
)

"%PYTHON%" "%~dp0main.py"
if errorlevel 1 pause
