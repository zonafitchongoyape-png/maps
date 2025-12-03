@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0"
echo.
echo --- Helper: push_to_github.bat ---
echo Working directory: %CD%
echo.


























































pauseecho Hecho.echo.)  git push -u origin main  git branch -M main  git remote add origin %REMOTEURL%  git remote remove origin 2>nul  )    exit /b 1    pause    echo URL remota vacía. Abortando.  if "%REMOTEURL%"=="" (  set /p REMOTEURL=Pegue la URL remota HTTPS (https://github.com/USER/REPO.git): ) else (  git push -u origin main  git branch -M main  )    gh repo create %GH_USER%/%GH_REPO% --public --source=. --remote=origin  ) else (    gh repo create %GH_USER%/%GH_REPO% --private --source=. --remote=origin  if "%GH_VIS%"=="private" (  echo Creando repo %GH_USER%/%GH_REPO%...  if "%GH_VIS%"=="" set GH_VIS=public  set /p GH_VIS=Visibilidad (public/private) [public]:   set /p GH_REPO=Nombre del repositorio (sin owner):   set /p GH_USER=Tu usuario de GitHub:   )    exit /b 1    pause    echo La CLI 'gh' no está instalada. Instale GitHub CLI o elija la opción 2.  if errorlevel 1 (  gh --version >nul 2>&1if "%CHOICE%"=="1" (set /p CHOICE=Opción [1/2]: echo 2) Proveer URL remota HTTPSecho 1) Usar GitHub CLI (gh)echo Elige método para crear el repo remoto:echo.git commit -m "%COMMITMSG%" 2>nul || echo No hay cambios para commitear.if "%COMMITMSG%"=="" set COMMITMSG=Initial commit - Visor de Ubicacionesset /p COMMITMSG=Mensaje de commit [Initial commit - Visor de Ubicaciones]: git add .)  git initif not exist .git (
nrem Initialize repo if needed and stage files)  exit /b 1  pause  echo Git no está instalado o no está en PATH. Instale Git antes de continuar.if errorlevel 1 (git --version >nul 2>&1nrem Check git availability