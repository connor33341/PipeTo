@echo off
echo %PATH% > Backup.txt
set "PATH=D:\GitHub\PipeTo\dist\;%PATH%"
echo %PATH% > Current.txt
pause