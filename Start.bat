@echo off
title Story2Video - Launcher
color 0B

echo.
echo  ======================================================
echo            Story2Video - Text to Video Engine          
echo            Edge TTS + Client-side Rendering            
echo  ======================================================
echo.

:: Luu thu muc goc
set "APP_DIR=%~dp0"
cd /d "%APP_DIR%"

:: Kiem tra Python
echo  [1/3] Kiem tra Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo.
    echo  [ERROR] Python chua duoc cai dat hoac chua co trong PATH!
    echo  Vui long cai dat Python 3.11+ tu https://python.org
    echo.
    pause
    exit /b 1
)
for /f "tokens=2 delims= " %%v in ('python --version 2^>^&1') do echo         Python %%v - OK

:: Cai dat thu vien neu chua co
echo.
echo  [2/3] Kiem tra thu vien can thiet...
python -c "import fastapi, uvicorn, edge_tts, dotenv" >nul 2>&1
if %errorlevel% neq 0 (
    echo         Dang cai dat thu vien, vui long doi...
    pip install fastapi uvicorn edge-tts python-dotenv
    if %errorlevel% neq 0 (
        color 0C
        echo.
        echo  [ERROR] Khong the cai dat thu vien! Kiem tra mang.
        echo.
        pause
        exit /b 1
    )
    echo         Cai dat xong!
) else (
    echo         Tat ca thu vien da san sang.
)

:: Khoi dong server
echo.
echo  [3/3] Khoi dong server...
echo.
echo  ------------------------------------------------------
echo    Story2Video dang chay tai: http://localhost:8001
echo    Bam Ctrl+C hoac tat cua so nay de xoa tien trinh.
echo  ------------------------------------------------------
echo.

:: Mo trinh duyet sau khi doi 2 giay
timeout /t 2 /nobreak >nul
start "" "http://localhost:8001"

:: Chay main.py
python main.py

echo.
echo  ======================================================
echo   Server da dung!
echo  ======================================================
echo.

:: Don dep tien trinh Python bi ket tren port 8001
for /f "tokens=5" %%p in ('netstat -aon ^| findstr ":8001" ^| findstr "LISTENING"') do (
    echo  Giai phong port 8001 (PID: %%p)...
    taskkill /f /pid %%p >nul 2>&1
)

echo  Hoan tat. Nhan phim bat ky de thoat.
pause
