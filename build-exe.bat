@echo off

pyinstaller src/main.py --workpath "./bin-int/debug/" --distpath "./bin/debug" --onefile --name "My First Game Jam Winter 2023 Submission"

@echo on