@echo off
color 0a

:a
SET BROWSER=firefox.exe
SET WAIT_TIME=2
START %BROWSER% -new-tab "wikipedia.org"
echo you have been trolled
timeout /t 1 >nul 2>&1
goto a
