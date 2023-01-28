@echo off

pyinstaller src/main.py --workpath ./bin-int/release/ --distpath ./bin/release --onefile --name "My First Game Jam Winter 2023 Submission" --noconsole

@echo on