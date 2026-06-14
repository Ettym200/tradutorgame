@echo off
chcp 65001 >nul
title Game Translator - Instalador

echo.
echo  ================================
echo   Game Translator - Instalando
echo  ================================
echo.

:: Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo  [ERRO] Python nao encontrado!
    echo.
    echo  Instale o Python em: https://www.python.org/downloads/
    echo  Marque a opcao "Add Python to PATH" durante a instalacao.
    echo.
    pause
    exit /b 1
)

echo  [OK] Python encontrado.
echo.
echo  Instalando dependencias...
echo.

pip install mss Pillow numpy openai anthropic

echo.
echo  ================================
echo   Instalacao concluida!
echo   Execute o arquivo: iniciar.bat
echo  ================================
echo.
pause
