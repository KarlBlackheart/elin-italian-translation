@echo off
REM ====================================================================
REM  Elin Mod Linker - Crea/Rimuove il collegamento nella cartella di gioco
REM  Consente di testare e pubblicare la mod su Steam senza duplicare file
REM ====================================================================

setlocal EnableDelayedExpansion

set "MOD_DIR=%~dp0"
if "%MOD_DIR:~-1%"=="\" set "MOD_DIR=%MOD_DIR:~0,-1%"

REM Ricerca del percorso di installazione di Elin
set "GAME_PACKAGE="

REM 1. Controlla prima il percorso predefinito / configurato
if exist "Z:\Giochi\SteamLibrary\steamapps\common\Elin" (
    set "GAME_PACKAGE=Z:\Giochi\SteamLibrary\steamapps\common\Elin\Package\Mod_Italian"
    goto PATH_FOUND
)
if exist "C:\Program Files (x86)\Steam\steamapps\common\Elin" (
    set "GAME_PACKAGE=C:\Program Files (x86)\Steam\steamapps\common\Elin\Package\Mod_Italian"
    goto PATH_FOUND
)
if exist "C:\Program Files\Steam\steamapps\common\Elin" (
    set "GAME_PACKAGE=C:\Program Files\Steam\steamapps\common\Elin\Package\Mod_Italian"
    goto PATH_FOUND
)
if exist "D:\SteamLibrary\steamapps\common\Elin" (
    set "GAME_PACKAGE=D:\SteamLibrary\steamapps\common\Elin\Package\Mod_Italian"
    goto PATH_FOUND
)

REM 2. Se non trovato nei percorsi comuni, richiedi all'utente
echo ====================================================================
echo   COLLEGAMENTO MOD ELIN - TRADUZIONE ITALIANA
echo ====================================================================
echo Impossibile trovare automaticamente la cartella di Elin.
set /p "USER_ELIN_PATH=Inserisci il percorso della cartella principale di Elin (es. C:\Giochi\Steam\steamapps\common\Elin): "
if exist "!USER_ELIN_PATH!\Package" (
    set "GAME_PACKAGE=!USER_ELIN_PATH!\Package\Mod_Italian"
    goto PATH_FOUND
) else (
    echo [ERRORE] La cartella indicata non contiene la sottocartella 'Package'.
    pause
    exit /b 1
)

:PATH_FOUND

if "%1"=="--unlink" goto UNLINK
if "%1"=="/u" goto UNLINK

echo ====================================================================
echo   COLLEGAMENTO MOD ELIN - TRADUZIONE ITALIANA
echo ====================================================================
echo Cartella Sorgente Mod:  %MOD_DIR%
echo Cartella Destinazione:  %GAME_PACKAGE%
echo.

if exist "%GAME_PACKAGE%" (
    echo [INFO] Il collegamento o la cartella esiste gia' in Elin/Package.
    echo Per rimuoverla esegui: link_mod.bat --unlink
    goto END
)

echo Creazione collegamento simbolico (Directory Junction)...
mklink /J "%GAME_PACKAGE%" "%MOD_DIR%"
if %ERRORLEVEL% equ 0 (
    echo.
    echo [SUCCESSO] Mod collegata con successo!
    echo Ora puoi avviare Elin da Steam:
    echo 1. Nel menu iniziale apri 'Mod' e attiva 'Traduzione Italiana'.
    echo 2. Nelle 'Impostazioni' seleziona la lingua 'Italiano'.
) else (
    echo.
    echo [ERRORE] Impossibile creare il collegamento. Verifica i permessi o il percorso.
)
goto END

:UNLINK
echo Rimozione del collegamento da Elin/Package...
if exist "%GAME_PACKAGE%" (
    rmdir "%GAME_PACKAGE%"
    echo [OK] Collegamento rimosso. I file originali del gioco non sono stati toccati.
) else (
    echo [INFO] Nessun collegamento trovato da rimuovere.
)

:END
echo.
