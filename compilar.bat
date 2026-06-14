@echo off
chcp 65001 >nul
title Game Translator - Compilando...

echo.
echo  ================================
echo   Compilando Game Translator
echo  ================================
echo.

pip install pyinstaller >nul 2>&1

echo  Gerando executavel...
echo.

python -m PyInstaller --noconfirm --onefile --windowed ^
  --name "GameTranslator" ^
  --icon NONE ^
  --add-data "code.jpeg;." ^
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
