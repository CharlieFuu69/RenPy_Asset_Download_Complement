## CharlieFuu69
## Ren'PyHub Download/Updater Plugin

## Script: Configuración de Ren'PyHub.

## © 2025 CharlieFuu69 - GNU GPL v3.0

## -------------------------------------------------------------------------- ##

## /!\ DOCUMENTACIÓN / READ THE DOCS /!\
##

################################################################################

# Declara los personajes usados en el juego como en el ejemplo:
define e = Character("Eileen")


label splashscreen:

  ## Llama al label con el flujo de trabajo de Ren'PyHub
  call seq_check_updates

  ## Si el label retorna, aquí van tus pantallas de bienvenida al juego,
  ## ejecutándose normalmente si no se encuentran actualizaciones.

  return


## Aquí comienza tu juego
label start:

    e "¡Parece que todo salió bien! ¡Gracias por probar Ren'PyHub!"

    return
