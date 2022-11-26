@ECHO OFF
Title Launching Zerum...
Start "" https://rsharmila20083.wixsite.com/zerum-uc
Set /p Input="UC Code: "
if "%input%"=="10010110 Fls" goto NU

:NU
START /MIN Zerum.py
EXIT
