@echo off

python -m venv venv

call venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements

echo.
echo Setup complete! To start the project, activate the virtual environment and run start.bat.
cls
pause
