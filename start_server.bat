@echo off
:loop
cd C:\AdityaOpenServer
python -m http.server 8008
python C:\_codes_Github\AdityaOpenServer\ip_fetch.py
pause
goto loop