# NÁUFRAGO

Prototipo roguelite de supervivencia 2D desarrollado en Python y Pygame. El jugador recorre un mundo continuo de cuatro biomas, reúne doblones, elige mejoras durante la partida y se enfrenta a jefes regionales antes del combate final contra Barbanegra al minuto 20.

## Ejecutar

Requiere Python 3.10 o superior y Pygame. Desde esta carpeta:

```powershell
python -m pip install -r requirements.txt
python main.py
```

En Windows también se puede abrir `jugar.bat`; el lanzador usa la instalación habitual de Python 3.12.
Si se cierra desde la terminal con **Ctrl+C**, la partida termina limpiamente y guarda los doblones reunidos.

## Controles

- **WASD** o **flechas**: moverse.
- **ESPACIO** o **SHIFT**: dash evasivo, con 0,2 s de invulnerabilidad y 3,5 s de recarga.
- **E**: activar un altar cuando estés a su lado.
- **ESC**: pausar o reanudar.
- **Ratón**: elegir las cartas de nivel, navegar los menús y ajustar el volumen.
- La pistola de chispa dispara automáticamente al objetivo más cercano.

## Bucle de juego

Las partidas comienzan en la playa central con nivel 1. Al conseguir experiencia, el juego se pausa y presenta tres mejoras con una rareza visual; las estadísticas de combate solo cambian durante esa partida. Cofres y barriles se destruyen con los ataques, y pueden soltar experiencia, doblones o curación. Los altares opcionales inician un desafío de supervivencia de 30 segundos y entregan un artefacto de la partida.

Al vencer enemigos se consiguen doblones. En el armario del menú se pueden desbloquear personajes y armas iniciales, además de comprar sombreros. El Capitán atrae más recursos, la Corsaria empieza con dagas perforantes y el Viejo Marinero resiste más y repele a sus atacantes. Los desbloqueos se guardan en `%USERPROFILE%\.naufrago\profile.json`.

## Mundo y amenazas

El mundo continuo ocupa 8400 × 3000 unidades, con una costa oval irregular recortada contra el agua. La orilla limita el movimiento y también afecta la colocación de enemigos, cofres y decoración:

- **Centro, playa y bosque costero**: cangrejos, esqueletos y el Kraken de la Orilla.
- **Este, Desierto de Calaveras**: serpientes, escorpiones, gaviotas y el Gólem de Arena. El calor reduce la regeneración al quedarse quieto.
- **Oeste, Tundra Helada**: osos mutantes y espectros; el hielo altera la inercia del movimiento.
- **Norte, Volcán Sombrío**: demonios de ceniza, espectros de fuego y meteoritos señalizados antes del impacto.

Los jefes regionales tienen dos fases y ataques telegrafiados. A los 20 minutos aparece Barbanegra; derrotarlo completa la partida. Los enemigos adaptan su salud y daño al tiempo sobrevivido y algunos aparecen como élites.

## Personajes y armas iniciales

El armario permite desbloquear y elegir personajes, armas iniciales y sombreros con doblones. Las armas secundarias que no se hayan elegido al comenzar pueden aparecer como cartas de mejora:

- **Pistola de chispa**: ataque automático de base.
- **Dagas arrojadizas**: proyectiles rápidos y penetrantes.
- **Bombas de pólvora**: explosión de área.
- **Bumerán de concha**: protección orbital.
- **Llama de ron**: deja fuego dañino al moverse.

## Estructura

- `main.py`: bucle principal, estados, interacción, combate y renderizado.
- `settings.py`: dimensiones, límites, biomas y catálogo de mejoras.
- `game_state.py`: validación y administración del estado activo.
- `player.py`, `enemy.py`, `boss.py`: entidades y estadísticas de personajes.
- `world.py`: selección de bioma según coordenadas del mundo.
- `ui.py`: colores de rareza y selección de rareza de cartas.
- `vfx.py`: partículas recicladas, destellos, pausa breve de impacto y vibración mínima de cámara.
- `profile.py`: persistencia y migración segura de cosméticos y desbloqueos.
- `tests/`: pruebas del juego y del perfil persistente.

El límite de partículas es de 60 elementos simultáneos; partículas, proyectiles, orbes y enemigos se reciclan para reducir asignaciones. Los efectos se recortan al área visible y el HUD suaviza la actualización de sus barras. La simulación usa pasos fijos de 1/60 s y limita el trabajo de recuperación tras una caída de frames; esto reduce picos, pero los FPS reales dependen del hardware.

## Pruebas

```powershell
python -m unittest discover -s tests -v
```

## Audio opcional

El juego no necesita recursos externos para iniciarse. Para añadir sonido, coloca archivos OGG en `assets/audio/`: `music.ogg`, `shot.ogg`, `damage.ogg`, `enemy.ogg`, `level.ogg` y `game_over.ogg`. La configuración permite ajustar los volúmenes general, de efectos y música.
