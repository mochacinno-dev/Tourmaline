@echo off
REM Tourma launcher — locate tourmaline.py in parent directories or PATH and execute it with provided args
setlocal

REM Start searching from the directory of this script
set "SEARCH_DIR=%~dp0"
set "FOUND="

REM Search up to 6 levels of parent directories for tourmaline.py
for /L %%i in (1,1,6) do (
  if exist "%SEARCH_DIR%tourmaline.py" (
    set "FOUND=%SEARCH_DIR%tourmaline.py"
    goto :found
  )
  for %%p in ("%SEARCH_DIR%..\") do set "SEARCH_DIR=%%~fpp"
)

REM If not found in parent directories, check in PATH
where tourmaline.py >nul 2>&1
if %ERRORLEVEL%==0 (
  for /f "usebackq delims=" %%f in (`where tourmaline.py`) do set "FOUND=%%f" & goto :found
)

REM Finally, check if 'tourmaline' command is available in PATH
where tourmaline >nul 2>&1
if %ERRORLEVEL%==0 (
  goto :foundcmd
)

REM If still not found, print error and exit
echo Error: could not find 'tourmaline.py' in script directory or PATH.
pause
endlocal & exit /b 1

REM If found, execute it with Python
:found
if defined FOUND (
  py -3 "%FOUND%" %* 2>nul || python "%FOUND%" %*
  endlocal & exit /b %ERRORLEVEL%
)

REM If 'tourmaline' command is available, use it
:foundcmd
tourmaline %*
endlocal & exit /b %ERRORLEVEL%