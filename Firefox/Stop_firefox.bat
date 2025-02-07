@echo off

set "batch_name=firefox.bat"

echo Recherche du processus en cours...
for /f "tokens=2 delims=," %%i in ('tasklist /fi "imagename eq cmd.exe" /v /fo csv ^| findstr /i "%batch_name%"') do (
    echo Arrêt du processus avec PID %%i...
    taskkill /PID %%i /F
)

echo Terminé.
pause
