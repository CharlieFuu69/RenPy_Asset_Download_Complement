## CharlieFuu69 Creations!
## Script Utility: Screens de ejemplo - Manipuladores de descargas.

## NOTA: Esta es la forma recomendada para ejecutar las descargas.

# ----------------------------------------------------------------------------------------------------------------- #
init:
    ## Algunos íconos de regalo para decorar la UI de descargas :3
    image icon_success = "radc/icon/ic_success.png"
    image icon_warning = "radc/icon/ic_warning.png"

screen download(url, savepath = None):
    ## Screen que ejecuta y muestra el progreso de descarga en la UI del juego

    modal True
    default dl = DownloadHandler(url, savepath)
    on "show" action Function(dl.start)

    ## ¿Finalizó la descarga?
    showif dl.status():
        frame:
            xysize(700, 300) align(0.5, 0.5)
            has vbox spacing 20 align(0.5, 0.5)

            ## ¿Ocurrió un error?
            if dl.runtime_exception():
                add "icon_warning" xalign 0.5
                text "Error al descargar el archivo." color "#FF0" xalign 0.5
                textbutton "Volver al Menú Principal" action MainMenu() xalign 0.5
            else:
                add "icon_success" xalign 0.5
                text "¡Descarga Completa!" color "#0A0" xalign 0.5
                textbutton "Reiniciar el juego" action Function(renpy.quit, relaunch = True, status = 0, save = False) xalign 0.5

    else:
        ## Descarga en curso
        frame:
            xysize(700, 300) align(0.5, 0.5)
            has vbox spacing 20  align(0.5, 0.5)

            text "Descargando recursos..." xalign 0.5
            text "Progreso : %.2f MB / %.2f MB" % (dl.sizelist[0], dl.sizelist[1]) xalign 0.5

            hbox:
                xalign 0.5 spacing 20

                bar value AnimatedValue(dl.gauge, 1.0):
                    xmaximum 350

                text "[[{0:.1%}]".format(dl.gauge)


screen mediafire_dl(shared_url, savepath = None):
    ## Esta screen se usa para cuando quieres descargar un archivo alojado en Mediafire.
    default dlfetch = SharedCloudGetFile(shared_url)
    on "show" action Function(dlfetch.start)

    ## ¿Finalizó la descarga?
    showif dlfetch.status():
        frame:
            xysize(700, 300) align(0.5, 0.5)
            has vbox spacing 20 align(0.5, 0.5)

            ## ¿Ocurrió un error?
            if dlfetch.runtime_exception():
                add "icon_warning" xalign 0.5
                text "Hubo un error mientras se obtenía la URL." color "#FF0" xalign 0.5
                textbutton "Volver al Menú Principal" action MainMenu() xalign 0.5
            else:
                timer 0.01 action [Hide("mediafire_dl"), Show("download", url = dlfetch.end_url(), savepath = savepath)]

    else:
        ## Descarga en curso
        frame:
            xysize(700, 300) align(0.5, 0.5)
            has vbox spacing 20  align(0.5, 0.5)

            text "Espera unos segundos." xalign 0.5
            text "Adquiriendo URL de descarga..." xalign 0.5
