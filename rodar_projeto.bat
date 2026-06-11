@echo off
chcp 65001 >nul
title NASA API — Iniciando...

echo.
echo  ╔══════════════════════════════════════╗
echo  ║         NASA API — Iniciando         ║
echo  ╚══════════════════════════════════════╝
echo.

:: ── Localiza a pasta do .bat e sobe para a raiz do projeto ──────────────────
cd /d "%~dp0"

if exist "API_Nasa" (
    cd API_Nasa
)

:: ── Verifica Python ──────────────────────────────────────────────────────────
python --version >nul 2>&1
if errorlevel 1 (
    echo  [ERRO] Python nao encontrado. Instale em https://www.python.org
    pause
    exit /b 1
)

:: ── Verifica Node ────────────────────────────────────────────────────────────
node --version >nul 2>&1
if errorlevel 1 (
    echo  [ERRO] Node.js nao encontrado. Instale em https://nodejs.org
    pause
    exit /b 1
)

:: ── Instala dependências Python se necessário ────────────────────────────────
echo  [1/3] Verificando dependencias Python...
pip show fastapi >nul 2>&1
if errorlevel 1 (
    echo        Instalando dependencias Python...
    pip install fastapi uvicorn requests python-dotenv
)
echo        OK
echo.

:: ── Instala dependências Node se necessário ──────────────────────────────────
echo  [2/3] Verificando dependencias Node...
if not exist "FrontEnd\node_modules" (
    echo        Instalando dependencias Node...
    cd FrontEnd
    npm install
    cd ..
)
echo        OK
echo.

:: ── Inicia Backend ───────────────────────────────────────────────────────────
echo  [3/3] Iniciando servidores...
echo.
echo  Backend  →  http://localhost:3000
echo  Frontend →  http://localhost:5173
echo.
echo  Feche esta janela para encerrar tudo.
echo  ──────────────────────────────────────────
echo.

start "NASA API — Backend" cmd /k "title NASA API — Backend && python -m BackEnd.main"

timeout /t 2 >nul

start "NASA API — Frontend" cmd /k "title NASA API — Frontend && cd FrontEnd && npm run dev"

timeout /t 3 >nul

start http://localhost:5173

echo  Servidores iniciados! O browser abrira automaticamente.
echo.
pause