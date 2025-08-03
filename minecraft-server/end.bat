@echo off
REM Stoppe den Minecraft-Server sauber

REM Sende den Befehl "stop" an die Konsole des Servers
echo stop > stop.txt

REM Optional: Warte kurz, dann alle java Prozesse beenden (unsauber)
timeout /t 5 /nobreak >nul
taskkill /im java.exe /f
