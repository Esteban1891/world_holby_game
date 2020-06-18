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

caminar = [pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run1.png'),
           pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run2.png'),
           pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run3.png'),
           pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run4.png'),
           pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run5.png'),
           pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run6.png'),
           pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run7.png'),
           pygame.image.load('personajes_background/heroes/PNG/Knight/Run/run8.png')]


saltar = [pygame.image.load('personajes_background/heroes/PNG/Knight/Jump/jump1.png'),
         pygame.image.load('personajes_background/heroes/PNG/Knight/Jump/jump2.png'),
         pygame.image.load('personajes_background/heroes/PNG/Knight/Jump/jump3.png'),
         pygame.image.load('personajes_background/heroes/PNG/Knight/Jump/jump4.png'),
         pygame.image.load('personajes_background/heroes/PNG/Knight/Jump/jump5.png'),
         pygame.image.load('personajes_background/heroes/PNG/Knight/Jump/jump6.png'),
         pygame.image.load('personajes_background/heroes/PNG/Knight/Jump/jump7.png')]

atacar = [pygame.image.load('personajes_background/heroes/PNG/Knight/Attack/attack0.png'),
          pygame.image.load('personajes_background/heroes/PNG/Knight/Attack/attack1.png'),
          pygame.image.load('personajes_background/heroes/PNG/Knight/Attack/attack2.png'),
          pygame.image.load('personajes_background/heroes/PNG/Knight/Attack/attack3.png'),
          pygame.image.load('personajes_background/heroes/PNG/Knight/Attack/attack4.png')]

#enemigo
enemigo_quieto = pygame.image.load('personajes_background/monster/PNG/demon/Idle1.png')

enemigo_caminar = [pygame.image.load('personajes_background/monster/PNG/demon/Walk1.png'),
                   pygame.image.load('personajes_background/monster/PNG/demon/Walk2.png'),
                   pygame.image.load('personajes_background/monster/PNG/demon/Walk3.png'),
                   pygame.image.load('personajes_background/monster/PNG/demon/Walk4.png'),
                   pygame.image.load('personajes_background/monster/PNG/demon/Walk5.png'),
                   pygame.image.load('personajes_background/monster/PNG/demon/Walk6.png')]

enemigo_atacar = [pygame.image.load('personajes_background/monster/PNG/demon/Attack1.png'),
                  pygame.image.load('personajes_background/monster/PNG/demon/Attack2.png'),
                  pygame.image.load('personajes_background/monster/PNG/demon/Attack3.png'),
                  pygame.image.load('personajes_background/monster/PNG/demon/Attack4.png')]


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


#Contador de salto
cuentaSalto = 0

#Contador de movimiento de ataque
contAtaque = 0

#Variables dirección
izquierda = False
derecha = False
atacando = False
mirar = "der"
salto = False

#Pasos
cuentaPasos = 0

#Movimiento
def recargaPantalla():
    #Variables globales
    global cuentaPasos
    global x
    global contAtaque
    global cuentaSalto

    #Fondo estático
    x_relativa = x % fondo.get_rect().width    
    PANTALLA.blit(fondo, (x_relativa, 0))
    
    PANTALLA.blit(pygame.transform.flip(enemigo_quieto, True, False), (-px, py))
    
    #Contador de pasos
    if cuentaPasos + 1 >= 8:
        cuentaPasos = 0
    
    #Contador de salto
    if cuentaSalto > 6:
        cuentaSalto = 0 

    #Contador de ataque
    if contAtaque > 4:
        contAtaque = 0    
     
    # Caminar hacia la izquierda
    if izquierda:      
        PANTALLA.blit(pygame.transform.flip(caminar[cuentaPasos], True, False), (int(px), int(py)))
        cuentaPasos += 1

    # Caminar hacia la derecha
    elif derecha:
        PANTALLA.blit(caminar[cuentaPasos], (int(px), int(py)))
        cuentaPasos += 1

    # Saltar
    elif salto:
        if mirar == "der":
            PANTALLA.blit(saltar[cuentaSalto], (int(px), int(py)))
        else:
            PANTALLA.blit(pygame.transform.flip(saltar[cuentaSalto], True, False), (int(px), int(py)))
        cuentaSalto += 1

    # Atacar
    elif atacando:
        if mirar == "der":        
            PANTALLA.blit(atacar[contAtaque], (int(px), int(py)))
        else:
            PANTALLA.blit(pygame.transform.flip(atacar[contAtaque], True, False), (int(px), int(py))) 
        contAtaque += 1           

    # Quedarse quieto
    else:
        if mirar == "der":        
            PANTALLA.blit(quieto, (int(px), int(py)))
        else:
            PANTALLA.blit(pygame.transform.flip(quieto, True, False), (int(px), int(py)))


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

    #Tecla LEFT - Moviemiento a la izquierda
    if keys[pygame.K_LEFT] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False
        mirar = "izq"

    #Tecla RIGHT - Moviemiento a la derecha
    elif keys[pygame.K_RIGHT] and px < 900 - velocidad - ancho:
        px += velocidad
        izquierda = False
        derecha = True
        mirar = "der"

    #Personaje quieto
    else:
        izquierda = False
        derecha = False
        atacando = False
        salto = False                      
    
    #Tecla G - Acción de atacar
    if keys[pygame.K_g]:
        atacando = True                            

    #Tecla UP - Moviemiento hacia arriba
    if keys[pygame.K_UP] and py > 100:
        py -= velocidad

    #Tecla DOWN - Moviemiento hacia abajo
    if keys[pygame.K_DOWN] and py < 300:
        py += velocidad

    #Tecla SPACE - Salto
    if keys[pygame.K_SPACE]:
        salto = True
        cuentaSalto += 1        

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