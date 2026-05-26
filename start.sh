#!/bin/bash
echo "==================================================="
echo "🩺 DIABETES INTELLIGENCE PLATFORM SETUP & RUN"
echo "==================================================="
echo

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed or not in your PATH."
    echo "Please install Python 3.10+ and try again."
    exit 1
fi

# Create virtual environment if it does not exist
if [ ! -d "venv" ]; then
    echo "[INFO] Creating Python Virtual Environment (venv)..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to create virtual environment."
        exit 1
    fi
    echo "[SUCCESS] Virtual environment created."
    echo
fi

# Activate virtual environment
echo "[INFO] Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to activate virtual environment."
    exit 1
fi
echo

# Install dependencies
echo "[INFO] Checking and installing dependencies from requirements.txt..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install dependencies."
    exit 1
fi
echo "[SUCCESS] All dependencies are up to date!"
echo

# Open browser automatically
echo "[INFO] Starting Flask Server..."
echo "[INFO] The application will be available at http://127.0.0.1:5000"

# Open browser depending on OS
if command -v xdg-open &> /dev/null; then
    sleep 1 && xdg-open http://127.0.0.1:5000 &
elif command -v open &> /dev/null; then
    sleep 1 && open http://127.0.0.1:5000 &
fi

# Run the application
python app.py
