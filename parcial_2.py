import pygame
from datos import lista
import json
'''
Nombre: Juan Sebastian
Apellido: Safatle
Division: 212-1
Fecha: 2/07/2024
Asignatura: Programacion I
Instancia: Segundo Examen Parcial

Desafío:

A. Analizar detenidamente el set de datos (puede agregarle más preguntas si así
lo desea).

B. Crear una pantalla de inicio, con 3 (tres) botones, “Jugar”, “Ver Puntajes”,
“Salir”, la misma deberá tener alguna imagen cubriendo completamente el
fondo y tener un sonido de fondo. Al apretar el botón jugar se iniciará el juego.
Opcional: Agregar un botón para activar/desactivar el sonido de fondo.

C. Crear 2 botones uno con la etiqueta “Pregunta”, otro con la etiqueta “Reiniciar”

D. Imprimir el Puntaje: 000 donde se va a ir acumulando el puntaje de las
respuestas correctas. Cada respuesta correcta suma 10 puntos.

E. Al hacer clic en el botón “Pregunta” debe mostrar las preguntas comenzando
por la primera y las tres opciones, cada clic en este botón pasa a la siguiente
pregunta.

F. Al hacer clic en una de las tres palabras que representa una de las tres
opciones, si es correcta, debe sumar el puntaje, reproducir un sonido de
respuesta correcta y dejar de mostrar las otras opciones.

G. Solo tiene 2 intentos para acertar la respuesta correcta y sumar puntos, si
agotó ambos intentos, deja de mostrar las opciones y no suma puntos. Al
elegir una respuesta incorrecta se reproducirá un sonido indicando el error y
se ocultará esa opción, obligando al usuario a elegir una de las dos restantes.

H. Al hacer clic en el botón “Reiniciar” debe mostrar las preguntas comenzando
por la primera y las tres opciones, cada clic pasa a la siguiente pregunta.
También debe reiniciar el puntaje.

I. Una vez terminado el juego se deberá pedirle el nombre al usuario, guardar
ese nombre con su puntaje en un archivo, y volver a la pantalla de inicio.

J. Al ingresar a la pantalla “Ver Puntajes”, se deberá mostrar los 3 (tres) mejores
puntajes ordenados de mayor a menor, junto con sus nombres de usuario
correspondientes. Debe haber un botón para volver al menú principal.

NOTAS:

- Tienen total libertad para utilizar los sonidos, imágenes, y animaciones
(opcional) alusivas, donde corresponda.

- El formato del archivo que se debe crear para guardar los puntajes
debe ser TXT, CSV o JSON.

- Se deben definir y utilizar funciones, y las mismas deben estar
documentadas e importadas desde otro archivo (biblioteca).
'''
pygame.init() #Se inicializa pygame
pygame.mixer.init()

preguntas = lista

#Botones
screen = pygame.display.set_mode([1280, 720]) #Se crea una ventana
rect_boton_jugar = pygame.Rect(490, 220, 290, 70)
rect_boton_puntaje = pygame.Rect(490, 330, 290, 70)
rect_boton_salir = pygame.Rect(490, 440, 290, 70)
rect_boton_pregunta = pygame.Rect(490, 300, 290, 70)
rect_boton_reiniciar = pygame.Rect(950, 30, 290, 70)
rect_boton_mute = pygame.Rect(15, 15, 190, 60)
rect_boton_a = pygame.Rect(490, 240, 290, 70)
rect_boton_b = pygame.Rect(490, 350, 290, 70)
rect_boton_c = pygame.Rect(490, 460, 290, 70)
rect_boton_preguntas_juego = pygame.Rect(490, 120, 390, 70)
rect_boton_volver = pygame.Rect(950, 30, 290, 70)

#Musica
sonido_fondo = pygame.mixer.Sound("Cosmic Dreams.wav")
sonido_fondo.set_volume(0.08)
sonido_correcta = pygame.mixer.Sound("GOOOOOOOOOOOOL.wav")
sonido_correcta.set_volume(0.04)
sonido_incorrecta = pygame.mixer.Sound("SONIDO RESPUESTA INCORRECTA 1-YTConverter.app.wav")
sonido_incorrecta.set_volume(0.02)

#Textos
font = pygame.font.SysFont("Arial Narrow", 50)
text_jugar = font.render("Jugar", True, (255, 255, 255))
text_puntaje = font.render("Puntaje", True, (255, 255, 255))
text_salir = font.render("Salir", True, (255, 255, 255))
text_mute = font.render("Music on", True, (255, 255, 255))
text_pregunta = font.render("Pregunta", True, (10, 10, 10))
text_reiniciar = font.render("Reiniciar", True, (10, 10, 10))
text_volver = font.render("Menu", True, (10, 10, 10))

#Imagenes
imagen_fondo = pygame.image.load("fondo preguntados.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, (1280, 720))
imagen_titulo = pygame.image.load("image.png")
imagen_titulo = pygame.transform.scale(imagen_titulo, (600, 100))
imagen_fondo_2 = pygame.image.load("image_preguntados.png")
imagen_fondo_2 = pygame.transform.scale(imagen_fondo_2, (1280, 720))
imagen_fondo_3 = pygame.image.load("fondo 3.jpg")
imagen_fondo_3 = pygame.transform.scale(imagen_fondo_3, (1280, 720))

#Contador
score = 0
intentos = 2

#Banderas
menu_principal = False
esta_jugando = False
musica = True
running = True
comienza_el_juego = False
mute = True
siguiente_pregunta = False
termino_el_juego = False
mostrar_score = False
scoreboard = False

#Lista de datos
pregunta_actual = 0

musica_txt = " Music on"
nombre = ""

def mostrar_preguntas(indice):

    
    screen.blit(imagen_fondo_2, (0,0))
    pygame.draw.rect(screen, (66, 177, 237), rect_boton_reiniciar, border_radius=15)
    pygame.draw.rect(screen, (66, 177, 237), rect_boton_a, border_radius=15)
    pygame.draw.rect(screen, (66, 177, 237), rect_boton_b, border_radius=15)
    pygame.draw.rect(screen, (66, 177, 237), rect_boton_c, border_radius=15)
    screen.blit(text_reiniciar, (1015, 50))
    
    pregunta_txt = font.render(lista[indice]['pregunta'], True, (10, 10, 10))
    screen.blit(pregunta_txt, (210, 120))
    option_a_text = font.render(f'A. {lista[indice]["a"]}', True, (10, 10, 10))
    screen.blit(option_a_text, (530, 260))
    option_b_text = font.render(f'B. {lista[indice]["b"]}', True, (10, 10, 10))
    screen.blit(option_b_text, (530, 370))
    option_c_text = font.render(f'C. {lista[indice]["c"]}', True, (10, 10, 10))
    screen.blit(option_c_text, (530, 480))
    score_txt = font.render(f"Score: {score}", True, (10, 10, 10))
    screen.blit(score_txt, (15, 15))
    pygame.display.flip()

def revisar_respuesta(indice, opcion_elegida):

    global score
    global intentos
    opcion_correcta = lista[indice]['correcta']
    opcion_elegida = ""

    if rect_boton_a.collidepoint(event.pos):
        opcion_elegida = 'a'
    if rect_boton_b.collidepoint(event.pos):
        opcion_elegida = 'b'
    if rect_boton_c.collidepoint(event.pos):
        opcion_elegida = 'c'
    if opcion_elegida ==  opcion_correcta:
        sonido_correcta.play(0)
        if intentos > 0:
            score = score + 10
        return True
    else:
        sonido_incorrecta.play(0)
        intentos -= 1
        return False

    
def leer_archivo_json():
    datos_json = {}
    with open("usuarios.json", "r") as archivo:
        datos_json = json.load(archivo)
    return datos_json

def guardar_usuarios(diccionario: dict):
    with open('usuarios.json', 'w') as f:
        json.dump(diccionario, f, indent= 4, ensure_ascii= False)

def borrar_letra(cadena: str):
    c_caracter = ""
    for i in range(len(cadena)-1):
        c_caracter += cadena[i]
    return c_caracter

def bubble_sort(datos):
    for i in range(len(datos)-1):
        for j in range(i+1, len(datos)):
            if datos[i]['score'] < datos[j]['score']:
                aux = datos[i]
                datos[i] = datos[j]
                datos[j] = aux
    return datos

datos_jugadores = leer_archivo_json()
opcion_elegida = ''

while running:
    
    # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        pressed_keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if mostrar_score == False:
            if esta_jugando == False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(f"Mouse down: {event.pos}")
                    if rect_boton_jugar.collidepoint(event.pos):
                        esta_jugando = True
                    
                    if rect_boton_puntaje.collidepoint(event.pos):
                        scoreboard = True
                        mostrar_score = True
                    if rect_boton_salir.collidepoint(event.pos):
                        running = False
                    
                    if rect_boton_mute.collidepoint(event.pos):
                        if mute == True:
                            musica_txt = "Music on"
                            mute = False
                            sonido_fondo.play(-1)
                        else:
                            musica_txt = "Music off"
                            mute = True
                            sonido_fondo.stop()
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rect_boton_pregunta.collidepoint(event.pos):
                        print("Empezo a jugar")
                        comienza_el_juego = True
                    if comienza_el_juego == True:
                        if rect_boton_a.collidepoint(event.pos):
                            if revisar_respuesta(pregunta_actual, opcion_elegida) == True:
                                print("Correcto")
                                siguiente_pregunta = True
                        if rect_boton_b.collidepoint(event.pos):
                            if revisar_respuesta(pregunta_actual, opcion_elegida) == True:
                                print("Correcto")
                                siguiente_pregunta = True
                        if rect_boton_c.collidepoint(event.pos):
                            if revisar_respuesta(pregunta_actual, opcion_elegida) == True:
                                print("Correcto")
                                siguiente_pregunta = True

                    if siguiente_pregunta == True:
                        if pregunta_actual < len(lista)-1:
                            pregunta_actual += 1
                            intentos = 2
                            siguiente_pregunta = False
                            termino_el_juego = False
                        else:
                            comienza_el_juego = False
                            termino_el_juego = True
                            mostrar_score = True
                    
                    if rect_boton_reiniciar.collidepoint(event.pos):
                        comienza_el_juego = False
                        score = 0
                        pregunta_actual = 0
                        intentos = 2
        if event.type == pygame.TEXTINPUT:
            nombre_usuario = event.text
            nombre += nombre_usuario
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_BACKSPACE:
                nombre = borrar_letra(nombre)
            if event.key == pygame.K_RETURN:
                mostrar_score = True
                scoreboard = True
                datos_usuario = {'usuario': nombre, 'score': score}
                datos_jugadores["scoreboard"].append(datos_usuario)
                guardar_usuarios(datos_jugadores)


    if musica == True:
        sonido_fondo.play(-1)
        musica = False
#menu principal
    if esta_jugando == False and termino_el_juego == False:
        screen.blit(imagen_fondo, (0,0))
        screen.blit(imagen_titulo, (345, 70))
        pygame.draw.rect(screen, (250, 183, 12), rect_boton_jugar, border_radius=15)
        pygame.draw.rect(screen, (250, 183, 12), rect_boton_puntaje, border_radius=15)
        pygame.draw.rect(screen, (250, 183, 12), rect_boton_salir, border_radius=15)
        pygame.draw.rect(screen, (250, 183, 12), rect_boton_mute, border_radius=15)
        screen.blit(text_jugar, (590, 240))
        screen.blit(text_puntaje, (580, 350))    
        screen.blit(text_salir, (590, 460))
        text_mute = font.render(musica_txt, True, (255, 255, 255))
        screen.blit(text_mute, (30, 30))

    elif esta_jugando == True and termino_el_juego == False:
        screen.blit(imagen_fondo_2, (0,0))
        pygame.draw.rect(screen, (66, 177, 237), rect_boton_pregunta, border_radius=15)
        pygame.draw.rect(screen, (66, 177, 237), rect_boton_reiniciar, border_radius=15)
        screen.blit(text_pregunta, (555, 320))
        screen.blit(text_reiniciar, (1015, 50))

    if comienza_el_juego == True :
        mostrar_preguntas(pregunta_actual)
        
    if termino_el_juego == True and mostrar_score == True :
        screen.blit(imagen_fondo_2, (0,0))
        termino_el_juego_txt = font.render("Has terminado el juego!!! Ingrese su nombre para guardar su resultado:", True, (10,10,10))
        screen.blit(termino_el_juego_txt, (50, 120))
        nombre_i_render = font.render(nombre, True, (10,10,10))
        screen.blit(nombre_i_render, (490, 300) )
    
    if scoreboard == True and mostrar_score == True:
        screen.blit(imagen_fondo_3, (0, 0))
        score_text = font.render("Estos son los 3 mejores jugadores:", True, (10,10,10))
        screen.blit(score_text, (400, 120))
        contador_puntajes = 0
        for datos in datos_jugadores['scoreboard']:
            bubble_sort(datos_jugadores['scoreboard'])
            mejores_txt = font.render(f"{contador_puntajes + 1}. {datos['usuario']}:  {datos['score']}", True, (10,10,10))
            if contador_puntajes < 3:
                pygame.draw.rect(screen,(250, 244, 130), (420, 200 + contador_puntajes * 110, 470, 70), border_radius=15)
                screen.blit(mejores_txt, (450, 220 + contador_puntajes * 110 ))
            contador_puntajes += 1

    pygame.display.flip()# Muestra los cambios en  la pantalla
pygame.quit() # Fin