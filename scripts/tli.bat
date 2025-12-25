@echo off
REM Tourma launcher — locate tourmaline.py in parent directories or PATH and execute it with provided args
setlocal

nset "SEARCH_DIR=%~dp0"
set "FOUND="

for /L %%i in (1,1,6) do (
  if exist "%SEARCH_DIR%tourmaline.py" (
    set "FOUND=%SEARCH_DIR%tourmaline.py"
    goto :found
  )
  for %%p in ("%SEARCH_DIR%..\") do set "SEARCH_DIR=%%~fpp"
)

nwhere tourmaline.py >nul 2>&1
if %ERRORLEVEL%==0 (
  for /f "usebackq delims=" %%f in (`where tourmaline.py`) do set "FOUND=%%f" & goto :found
)

nwhere tourmaline >nul 2>&1
if %ERRORLEVEL%==0 (
  goto :foundcmd
)

necho Error: could not find 'tourmaline.py' in script directory or PATH.
pause
endlocal & exit /b 1

n:found
if defined FOUND (
  py -3 "%FOUND%" %* 2>nul || python "%FOUND%" %*
  endlocal & exit /b %ERRORLEVEL%
)

n:foundcmd
tourmaline %*
endlocal & exit /b %ERRORLEVEL%