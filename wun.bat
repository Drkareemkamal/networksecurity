net stop bits
net stop wuauserv
net stop appidsvc
net stop cryptsvc

Del "%ALLUSERSPROFILE%\Application Data\Microsoft\Network\Downloader\qmgr*.dat"

rmdir %systemroot%\SoftwareDistribution /s /q
rmdir %systemroot%\System32\catroot2 /s /q

net start bits
net start wuauserv
net start appidsvc
net start cryptsvc

echo Windows Update components have been reset.
pause
