@echo off
title Diabetes Intelligence Platform Startup
echo ===================================================
echo 🩺 DIABETES INTELLIGENCE PLATFORM SETUP ^& RUN
echo ===================================================
echo.

:: Check Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not added to your PATH environment variable.
    echo Please install Python 3.10+ from https://www.python.org/ and try again.
    pause
    exit /b 1
)

:: Create virtual environment if it does not exist
if not exist venv (
    echo [INFO] Creating Python Virtual Environment (venv)...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to create virtual environment.
        pause
        exit /b 1
    )
    echo [SUCCESS] Virtual environment created.
    echo.
)

:: Activate virtual environment
echo [INFO] Activating virtual environment...
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate virtual environment.
    pause
    exit /b 1
)
echo.

:: Install dependencies
echo [INFO] Checking and installing dependencies from requirements.txt...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies.
    pause
    exit /b 1
)
echo [SUCCESS] All dependencies are up to date!
echo.

:: Open browser automatically in 2 seconds in the background
echo [INFO] Starting Flask Server...
echo [INFO] The browser will open automatically at http://127.0.0.1:5000
start "" http://127.0.0.1:5000

:: Run the application
python app.py

pause
