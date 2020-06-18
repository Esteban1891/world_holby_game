import pygame
import sys

#Iniciación de Pygame
pygame.init()

#Pantalla - ventana
W, H = 760, 428
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption('Holby game')
icono = pygame.image.load('personajes_background/icon.png')
pygame.display.set_icon(icono)

#Fondo del juego
fondo = pygame.image.load('personajes_background/backgroung_PNG/Battleground2/Bright/Battleground2.png')

#Música de fondo
pygame.mixer.music.load('sonido/intergalactic_odyssey.ogg')
pygame.mixer.music.play(-1)


#Personaje
quieto = pygame.image.load('personajes_background/heroes/PNG/Knight/knight.png')

caminaDerecha = [pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run1.png'),
                 pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run2.png'),
                 pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run3.png'),
                 pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run4.png'),
                 pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run5.png'),
                 pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run6.png'),
                 pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run7.png'),
                 pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run8.png')]

caminaIzquierda = [pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run1.png'),
                   pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run2.png'),
                   pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run3.png'),
                   pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run4.png'),
                   pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run5.png'),
                   pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run6.png'),
                   pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run7.png'),
                   pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run8.png')]

salta = [pygame.image.load('personajes_background/heroes/PNG/Knight/Jump/jump1.png'),
         pygame.image.load('personajes_background/heroes/PNG/Knight/Jump/jump2.png'),
         pygame.image.load('personajes_background/heroes/PNG/Knight/Jump/jump3.png'),
         pygame.image.load('personajes_background/heroes/PNG/Knight/Jump/jump4.png'),
         pygame.image.load('personajes_background/heroes/PNG/Knight/Jump/jump5.png'),
         pygame.image.load('personajes_background/heroes/PNG/Knight/Jump/jump6.png'),
         pygame.image.load('personajes_background/heroes/PNG/Knight/Jump/jump7.png')]

#Sonido
sonido_arriba = pygame.image.load('sonido/volume_up.png')
sonido_abajo = pygame.image.load('sonido/volume_down.png')
sonido_mute = pygame.image.load('sonido/volume_muted.png')
sonido_max = pygame.image.load('sonido/volume_max.png')

x=0
px = 50
py = 200
ancho = 40
velocidad = 10

#Control de FPS
reloj = pygame.time.Clock()

#Variables salto
salto = False
#Contador de salto
cuentaSalto = 10

#Variables dirección
izquierda = False
derecha = False

#Pasos
cuentaPasos = 0

#Movimiento
def recargaPantalla():
    #Variables globales
    global cuentaPasos
    global x

    #Fondo en movimiento
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < W:
        PANTALLA.blit(fondo, (x_relativa, 0))
    x -= 5
    #Contador de pasos
    if cuentaPasos + 1 >= 8:
        cuentaPasos = 0
    #Movimiento a la izquierda
    if izquierda:
        PANTALLA.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    # Movimiento a la derecha
    elif derecha:
        PANTALLA.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    elif salto + 1 >= 7:
        PANTALLA.blit(salta[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    else:
        PANTALLA.blit(quieto,(int(px), int(py)))

ejecuta = True

#Bucle de acciones y controles
while ejecuta:
    #FPS
    reloj.tick(18)

    #Bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    #Opción tecla pulsada
    keys = pygame.key.get_pressed()

    #Tecla A - Moviemiento a la izquierda
    if keys[pygame.K_a] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False

    #Tecla D - Moviemiento a la derecha
    elif keys[pygame.K_d] and px < 900 - velocidad - ancho:
        px += velocidad
        izquierda = False
        derecha = True

    #Personaje quieto
    else:
        izquierda = False
        derecha = False
        cuentaPasos = 0

    #Tecla W - Moviemiento hacia arriba
    if keys[pygame.K_w] and py > 100:
        py -= velocidad

    #Tecla S - Moviemiento hacia abajo
    if keys[pygame.K_s] and py < 300:
        py += velocidad
    #Tecla SPACE - Salto
    if not (salto):
        if keys[pygame.K_SPACE]:
            salto = True
            izquierda = False
            derecha = False
            cuentaPasos = 0
    else:
        if cuentaSalto >= -10:
            py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
            cuentaSalto -= 1
        else:
            cuentaSalto = 10
            salto = False

    # Control del audio
    #Baja volumen
    if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
        PANTALLA.blit(sonido_abajo, (850, 25))
    elif keys[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
        PANTALLA.blit(sonido_mute, (850, 25))

    #Sube volumen
    if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        PANTALLA.blit(sonido_arriba, (850, 25))
    elif keys [pygame.K_0] and pygame.mixer.music.get_volume() == 1.0:
            PANTALLA.blit(sonido_max, (850, 25))

    #Desactivar sonido
    elif keys[pygame.K_m]:
        pygame.mixer.music.set_volume(0.0)
        PANTALLA.blit(sonido_mute, (850, 25))

    #Reactivar sonido
    elif keys[pygame.K_COMMA]:
        pygame.mixer.music.set_volume(1.0)
        PANTALLA.blit(sonido_max, (850, 25))

    # Actualización de la ventana
    pygame.display.update()
    #Llamada a la función de actualización de la ventana
    recargaPantalla()

#Salida del juego
pygame.quit()