@echo off
echo Setting up your Web Forum APP...
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
echo Flask installed successfully.
del setup.bat
echo @echo off > app.bat
echo call venv\Scripts\activate >> app.bat
echo python app.py >> app.bat
echo exit >> app.bat
rename app.bat app.exe
echo Setup complete! Run the app using app.exe.
