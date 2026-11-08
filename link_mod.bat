@echo off
REM ====================================================================
REM  Elin Mod Linker - Crea/Rimuove il collegamento nella cartella di gioco
REM  Consente di testare e pubblicare la mod su Steam senza duplicare file
REM ====================================================================

set "GAME_PACKAGE=Z:\Giochi\SteamLibrary\steamapps\common\Elin\Package\Mod_Italian"
set "MOD_DIR=%~dp0"
REM Rimuovi trailing backslash
if "%MOD_DIR:~-1%"=="\" set "MOD_DIR=%MOD_DIR:~0,-1%"

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
    echo Ora puoi avviare Elin:
    echo 1. Troverai 'Traduzione Italiana' nel menu 'Mod' del gioco.
    echo 2. Nelle 'Opzioni' potrai selezionare la lingua 'Italiano'.
    echo 3. Potrai anche cliccare 'Pubblica' per caricarla su Steam Workshop!
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
pause
