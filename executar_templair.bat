@echo off
title Iniciando Templair SOC Assistant...
echo ===================================================
echo            INICIANDO PAINEL TEMPLAIR AI            
echo ===================================================
echo.

:: Garante que o script rode a partir do diretorio onde o .bat esta salvo
cd /d "%~dp0"

:: Executa o app.py diretamente (ja que o .bat e o app estao na mesma pasta)
python -m streamlit run app.py

pause