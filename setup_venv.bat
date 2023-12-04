@echo on
set VENV_DIR=..\virenvproject
python -m venv %VENV_DIR%
%VENV_DIR%\Scripts\Activate.ps1
pip install -r CPE334Project\requirements.txt
