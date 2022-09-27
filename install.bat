@ECHO OFF

cd C:\%HOMEPATH%\Desktop
mkdir pybot

cd C:%HOMEPATH%\AppData\Local\Programs\Python\Python38
python --version>NUL

if %ERRORLEVEL% == 0 goto pythonInstalled 
ECHO Downloading Python
curl https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe -o python_install.exe

ECHO Installing Python
python_install.exe /quiet
del python_install.exe

ECHO Editing PATH Variables
::setx path "%path%;C:%HOMEPATH%\AppData\Local\Programs\Python\Python38\Scripts"
::setx /M path "%path%;C:%HOMEPATH%\AppData\Local\Programs\Python\Python38"

ECHO Python installed
ECHO Upgrading PIP
cd C:%HOMEPATH%\AppData\Local\Programs\Python\Python38
python -m pip install --upgrade pip

goto:pythonInstalled

:pythonInstalled 

ECHO Installed Python Version:
cd C:%HOMEPATH%\AppData\Local\Programs\Python\Python38
python --version

ECHO Grabbing Python Modules...

cd C:%HOMEPATH%\AppData\Local\Programs\Python\Python38\Scripts
pip install bs4
pip install requests
pip install openpyxl

ECHO Downloads Complete

cd C:%HOMEPATH%\AppData\Local\Programs\Python\Python38
python "C:\Program Files\spaceCRAFT_GUI\testing_imgui.py"

PAUSE