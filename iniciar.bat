@echo off
chcp 65001 >nul
title Game Translator
cd /d "%~dp0"
python main.py
if errorlevel 1 (
    echo.
    echo  Ocorreu um erro. Execute instalar.bat primeiro.
    pause
)
