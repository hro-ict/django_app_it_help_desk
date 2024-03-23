@echo off
git add .
set /p commit= Type commit
git commit -m   "%commit%"
git push  -u origin main