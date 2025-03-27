@echo off
:loop
python C:\_codes_Github\LocalServer\ip_fetch.py
@REM cd C:\AdityaOpenServer
cd C:\Users\Aditya\Pictures\Screenshots
python -m http.server 8008
pause
goto loop