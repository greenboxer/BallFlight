rem Requires:
rem * pyinstaller 5.0.dev0 for build
rem * matplotlib 3.5.1
pyinstaller --noconsole --noconfirm --clean main.py


if not exist "build" mkdir build
if exist "build\ballflight" rmdir /s /q builds\ballflight

move /y .\dist\main .\dist\ballflight
rmdir /s /q build

cd dist
tar -czf ballflight.tar.gz ballflight

rmdir /s /q main
rmdir /s /q ballflight