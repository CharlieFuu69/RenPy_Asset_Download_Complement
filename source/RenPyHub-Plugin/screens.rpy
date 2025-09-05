## CharlieFuu69
## Ren'PyHub Plugin

## Script: Diseño de UI prefabricado para Ren'PyHub.

## © 2025 CharlieFuu69 - GNU GPL v3.0

################################################################################

## /!\ DOCUMENTACIÓN / READ THE DOCS /!\
## Versión en Español:
## https://github.com/CharlieFuu69/RenPyHub-Plugin/wiki/quickstart%E2%80%90esp#2-qu%C3%A9-scripts-contiene-el-proyecto-de-prueba
##
## English version:
## <URL>

################################################################################

## -------------------------------------------------------------------------- ##
## Screens de procesos

screen check_updates():
    style_prefix "msg_window"

    ## Ejecuta el hilo de comprobación de actualizaciones
    on "show" action Function(renpy.invoke_in_thread, fn=cdn.start)

    ## ¿Terminó el proceso de verificación?
    if cdn.process_done:
        ## ¿Ocurrió un error durante el proceso?
        if cdn.exc_output:
            timer 0.001:
                action [Hide("check_updates"),
                        Show("msg_dl_network_error",
                            exc_content=cdn.exc_output,
                            target_label="seq_check_updates")]

        ## Continúa con el flujo de trabajo
        else:
            timer 0.001 action [Hide("check_updates"), Return()]

    else:
        frame:
            text _("Buscando actualizaciones...")


screen download_assets():
    style_prefix "download"

    ## Ejecuta el hilo de descarga de datos
    on "show" action Function(renpy.invoke_in_thread, fn=download.start)

    ## ¿Terminó la descarga de datos?
    if download.process_done:
        ## ¿Ocurrió un error durante el proceso?
        if download.exc_output:
            timer 0.001:
                action [Hide("download_assets"),
                        Show("msg_dl_network_error",
                            exc_content=download.exc_output,
                            target_label="seq_download")]

        ## Continúa con el flujo de trabajo
        else:
            timer 0.01 action [Hide("download_assets"), Return()]

    else:
        ## Barra de progreso de descarga (Inferior)
        frame:
            has vbox

            label _("DESCARGANDO RECURSOS...")

            null height 40

            ## Barras de progreso
            vbox spacing 8:
                ## Progreso como texto
                text download.fmt_callback()

                ## Progreso del paquete actual
                bar:
                    value StaticValue(download.pkg_received, download.pkg_total or 0.1)

                ## Progreso de la descarga general
                bar:
                    value StaticValue(download.received, download.total or 0.1)


## Esto declara a `download_assets` como una screen que debe refrescarse
## de manera constante.
init python:
    config.per_frame_screens.append("download_assets")


## -------------------------------------------------------------------------- ##
## Screens de notificación

screen msg_dl_confirmation():
    style_prefix "msg_window"
    modal True

    frame:
        has vbox

        label _("CONFIRMACIÓN DE DESCARGA")

        vbox spacing 3:
            text _("TAMAÑO DE DESCARGA")
            add Solid("#FFF", xysize=(150, 2))
            text datasize(cdn.download_size) size 22

        text _("Esta descarga contiene los recursos del juego.")
        text _("La velocidad de descarga puede variar en función del tráfico en GitHub, o de la estabilidad de tu conexión.")

        hbox:
            textbutton _("Iniciar descarga"):
                action [Hide("msg_dl_confirmation"), Return()]


screen msg_global_update():
    style_prefix "msg_window"
    modal True

    frame:
        has vbox

        label _("ACTUALIZACIÓN GLOBAL NECESARIA")

        text _("Hay una nueva versión disponible del juego (v%(version)s).") %(cdn.info)
        text _("Presiona en \"Abrir sitio web\" para ir a la página web del desarrollador.")

        hbox:
            textbutton _("Abrir sitio web"):
                action OpenURL(GAME_WEBSITE_URL), Quit(confirm=False)

            textbutton _("Cerrar el juego"):
                action Quit(confirm=False)


screen msg_maintenance_notice():
    style_prefix "msg_window"
    modal True

    frame:
        has vbox

        label _("MANTENIMIENTO PROGRAMADO")

        text _("En estos momentos se están ejecutando labores de mantenimiento.")
        text _("Fecha/hora de puesta en marcha estimada:")
        text "%(restart_date)s" %(cdn.info) color "#FF0"

        hbox:
            textbutton _("Cerrar el juego"):
                action Quit(confirm=False)


screen msg_dl_network_error(exc_content, target_label):
    style_prefix "msg_window"
    modal True

    frame:
        has vbox

        label _("ERROR DE CONEXIÓN")
        text exc_content

        hbox:
            textbutton _("Reintentar"):
                action Hide("msg_dl_network_error"), Jump(target_label)

            textbutton _("Cerrar el juego"):
                action Quit(confirm=False)


screen msg_dl_complete():
    style_prefix "msg_window"
    modal True

    frame:
        has vbox

        label _("DESCARGA FINALIZADA")

        text _("Todos los paquetes se descargaron correctamente.")
        text _("Presiona \"Reiniciar el juego\" para aplicar los cambios de los archivos descargados.")

        hbox:
            textbutton _("Reiniciar el juego"):
                action Hide("msg_dl_complete"), Return()


## -------------------------------------------------------------------------- ##
## Estilos

## Prefijo "msg_window"
style msg_window_frame:
    background Frame("RenPyHub-Plugin/ui_frame_notify.png", 14, 14, 14, 14)
    padding(25, 15, 25, 15)
    align(0.5, 0.5)
    xmaximum 700

style msg_window_vbox:
    xalign 0.5
    spacing 15

style msg_window_hbox:
    xalign 0.5
    spacing 30

style msg_window_label:
    xalign 0.5

style msg_window_label_text:
    color "#CCFF00"
    size 18

style msg_window_text:
    color "#FFFFFF"
    size 14
    xalign 0.5
    text_align 0.5

style msg_window_button:
    idle_background Frame(Solid("#444444"))
    hover_background Frame(Solid("#CCFF00"))
    padding(15, 2, 15, 2)
    yalign 0.5

style msg_window_button_text:
    idle_color "#FFFFFF"
    hover_color "#000000"
    size 16
    align(0.5, 0.5)


## Prefijo "download"
style download_frame is msg_window_frame
style download_vbox is msg_window_vbox
style download_label is msg_window_label
style download_label_text is msg_window_label_text
style download_text is msg_window_text:
    xalign 0.0

style download_bar:
    left_bar Solid("#CCFF00")
    right_bar Solid("#444444")
    ysize 4
