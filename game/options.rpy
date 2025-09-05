## Este archivo contiene opciones que pueden cambiarse para personalizar el
## juego.
##
## Las líneas que empiezan con doble '#' son comentarios, no deben ser
## descomentadas. Las líneas que empiezan con simple '#' son código comentado,
## puedes descomentarlas si es apropiado.


## Básico ######################################################################

## Nombre del juego en forma legible. Usado en el título de la ventana del
## juego, en la interfaz y en los informes de error.
##
## El _() que rodea la cadena de texto la señala como traducible.

define config.name = _("Ren'PyHub Sample Project")


## Determina si el título dado más arriba se muestra en el menú principal.
## Ajústalo a 'False' para ocultar el título.

define gui.show_name = True


## Versión del juego.

define config.version = "1.0"


## Texto situado en la pantalla 'Acerca de' del juego. Sitúa el texto entre
## comillas triples y deja una línea en blanco entre párrafos.

define gui.about = _p("""
""")


## Nombre breve del juego para ejecutables y directorios en la distribución.
## Debe contener solo carácteres ASCII, sin espacios, comas o puntos y coma.

define build.name = "RenPyHub_DAM_Plugin"


## Sonidos y música ############################################################

## Estas tres variables controlan, entre otras cosas, qué mezcladores se
## muestran al reproductor de forma predeterminada. Establecer uno de estos en
## False ocultará el mezclador apropiado.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## Para permitir al usuario probar el volumen de los canales de sonido o voz,
## descomenta la línea más abajo y ajústala a un sonido de ejemplo.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Descomenta la línea siguiente para ajustar un archivo de audio que sonará
## en el menú principal. Este archivo seguirá sonando en el juego hasta que sea
## detenido o se reproduzca otro archivo.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transiciones ################################################################
##
## Estas variables ajustan transiciones usadas ante ciertos eventos. Cada
## variable debe indicar una transición o bien 'None', cuando no se desea usar
## ninguna transición.

## Entrar o salir del manú del juego.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Entre pantallas del menú del juego.

define config.intra_transition = dissolve


## Transición tras la carga de una partida.

define config.after_load_transition = None


## Transición de acceso al menú principal tras finalizar el juego.

define config.end_game_transition = None


## No existe la variable que ajusta la transición cuando el juego comienza.
## Para ello se usa la sentencia 'with' al mostrar la escena inicial.


## Gestión de ventanas #########################################################
##
## Esto controla cuándo se muestra la ventana de diálogo. Si es "show", es
## siempre visible. Si es "hide", solo se muestra cuando hay diálogo presente.
## Si es "auto", la ventana se esconde antes de las sentencias 'scene' y se
## muestra de nuevo cuando hay diálogo que presentar.
##
## Una vez comenzado el juego, esto se puede ajustar con las sentencias "window
## show", "window hide", y "window auto".

define config.window = "auto"


## Transiciones usadas para mostrar o esconder la ventana de diálogo

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preferencias por defecto ####################################################

## Controla la velocidad del texto por defecto. El valor por defecto 0 indica
## infinito; cualquier otro número indica el número de caracteres por segundo
## que se mostrarán.

default preferences.text_cps = 0


## El retraso por defecto del auto-avance. Números más grandes indican esperas
## mayores. El rango válido es 0-30.

default preferences.afm_time = 15


## Directorio de guardado ######################################################
##
## Controla el lugar en el que Ren'Py colocará los archivos de guardado,
## dependiendo de la plataforma.
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Normalmente, este valor no debe ser modificado. Si lo es, debe ser siempre
## una cadena literal y no una expresión.

define config.save_directory = "RenPyHub_DAM_Plugin-1756709732"


## Icono #######################################################################
##
## El icono mostrado en la barra de tareas.

define config.window_icon = "gui/window_icon.png"


## Configuración de 'Build' ####################################################
##
## Esta sección contrla cómo Ren'Py convierte el proyecto en archivos para la
## distribución.

init python:

    ## Las funciones siguientes toman patrones de archivos. No son relevantes
    ## las mayúsculas o minúsculas. Son relativos al directorio base, con o sin
    ## una / inicial. Si corresponden más de un patrón, se usa el primero.
    ##
    ## En un patrón:
    ##
    ## / es el separador de directorios.
    ##
    ## * corresponde a todos los carácteres, excepto el separador de
    ##   directorios.
    ##
    ## ** corresponde a todos los carácteres, incluynedo el separador de
    ##    directorios.
    ##
    ## Por ejemplo, "*.txt" corresponde a los archivos .txt en el directorio
    ## de base, "game/**.ogg" corresponde a los archivos .ogg del directorio
    ## 'game' y sus subdirectorios y "**.psd" corresponde a los archivos .psd en
    ## cualquier parte del proyecto.

    ## Clasifica archivos como 'None' para excluirlos de la distribución.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Para archivar, se clasifican como 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Los archivos que corresponden a patrones de documentation se duplican en
    ## la distribución de mac; aparecerán en los archivos app y zip.

    build.documentation('*.html')
    build.documentation('*.txt')


## Se necesita una clave de licencia de Google Play para realizar compras
## dentro de la aplicación. Se puede encontrar en la consola de desarrollador
## de Google Play, en "Monetizar" > "Configuración de la monetización" >
## "Licencias".

# define build.google_play_key = "..."


## Los nombres de usuario y de proyecto asociados con un proyecto itch.io,
## separados por una barra.

# define build.itch_project = "renpytom/test-project"
