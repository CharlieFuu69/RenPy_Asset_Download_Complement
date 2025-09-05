## CharlieFuu69
## Ren'PyHub Plugin

## Script: Flujo de trabajo de Ren'PyHub.

## © 2025 CharlieFuu69 - GNU GPL v3.0

################################################################################


## -------------------------------------------------------------------------- ##
## Flujo de trabajo de Ren'PyHub

## Comprobación de actualizaciones
label seq_check_updates:

    ## Instancia a la clase UpdateHandler()
    $ cdn = UpdateHandler()

    call screen check_updates

    ## ¿El ejecutable necesita actualizarse?
    if cdn.exit == "update":
        call screen msg_global_update

    ## ¿Hay una fase de mantenimiento?
    elif cdn.exit == "offline":
        call screen msg_maintenance_notice

    ## ¿Hay archivos pendientes de actualizar o descargar?
    elif cdn.exit == "download":
        call screen msg_dl_confirmation

        ## Instancia la clase DownloadHandler() para realizar la descarga
        $ download = DownloadHandler(
            packages=cdn.downloads,  ## La lista de paquetes pendientes de descargar
            rootdir=config.gamedir,  ## Aapunta a la carpeta /game
            bufsize=25600            ## Búfer: 25 kiB
        )

        ## Salta a la secuencia de descargas
        jump seq_download


    ## Si no se encuentran actualizaciones, retorna al flujo del `label splashscreen`
    else:
        return


## Secuencia de descarga de assets
label seq_download:
    call screen download_assets
    call screen msg_dl_complete

    ## Cierra el juego y lo ejecuta de nuevo
    $ renpy.quit(save=False, relaunch=True)
