@echo off
chcp 65001 >nul
title Game Translator - Compilando...

echo.
echo  ================================
echo   Compilando Game Translator
echo  ================================
echo.

pip install pyinstaller >nul 2>&1

echo  Convertendo icone...
python -c "from PIL import Image; img = Image.open('incone.png'); img.save('incone.ico', format='ICO', sizes=[(256,256),(128,128),(64,64),(32,32),(16,16)])"

echo  Gerando executavel...
echo.

python -m PyInstaller --noconfirm --onefile --windowed ^
  --name "GameTranslator" ^
  --icon "incone.ico" ^
  --add-data "code.jpeg;." ^
  --add-data "incone.png;." ^
  --hidden-import PIL ^
  --hidden-import PIL.ImageTk ^
  --hidden-import mss ^
  --hidden-import openai ^
  --hidden-import anthropic ^
  --hidden-import keyboard ^
  main.py

echo.
if exist "dist\GameTranslator.exe" (
    echo  ================================
    echo   Sucesso!
    echo   Arquivo: dist\GameTranslator.exe
    echo   Esse e o arquivo para distribuir.
    echo  ================================
) else (
    echo  [ERRO] Compilacao falhou.
)
echo.
pause
