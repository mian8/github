echo off
echo ok

::md %windir%\JJJ
md jj

rd jj

pause>nul

cls

ping -n 5 192.168.56.1

pause>nul