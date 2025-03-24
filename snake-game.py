import turtle
import time
import random

delay = 0.1
puntos = 0
max_puntos = 0

# Configuración de la ventana de juego
ventana = turtle.Screen()
ventana.title("Snake Game")
ventana.bgcolor("black")
ventana.setup(width=600, height=600)
ventana.tracer(0)

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "Stop"

# Comida de la serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

segmentos = []

# Texto de puntuación
texto_puntos = turtle.Turtle()
texto_puntos.speed(0)
texto_puntos.color("white")
texto_puntos.penup()
texto_puntos.hideturtle()
texto_puntos.goto(0, 260)
texto_puntos.write("Puntos: 0  Máx Puntos: 0", align="center", font=("Courier", 18, "normal"))

# Funciones de movimiento de la serpiente
def arriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"

def abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"

def izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"

def derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"

def mover():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# Teclado
ventana.listen()
ventana.onkeypress(arriba, "w")
ventana.onkeypress(abajo, "s")
ventana.onkeypress(izquierda, "a")
ventana.onkeypress(derecha, "d")

# Bucle principal del juego
while True:
    ventana.update()

    # Verificar colisiones con los bordes
    if cabeza.xcor() > 290 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "Stop"

        for segmento in segmentos:
            segmento.goto(1000, 1000)

        segmentos.clear()

        puntos = 0
        delay = 0.1

        texto_puntos.clear()
        texto_puntos.write(f"Puntos: {puntos}  Máx Puntos: {max_puntos}", align="center", font=("Courier", 18, "normal"))

    # Verificar colisiones con la comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        delay -= 0.001

        puntos += 10

        if puntos > max_puntos:
            max_puntos = puntos

        texto_puntos.clear()
        texto_puntos.write(f"Puntos: {puntos}  Máx Puntos: {max_puntos}", align="center", font=("Courier", 18, "normal"))

    # Mover los segmentos de la serpiente en orden inverso
    for index in range(len(segmentos)-1, 0, -1):
        x = segmentos[index-1].xcor()
        y = segmentos[index-1].ycor()
        segmentos[index].goto(x, y)

    # Mover segmento 0 a donde está la cabeza
    if len(segmentos) > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mover()

    # Verificar colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "Stop"

            for segmento in segmentos:
                segmento.goto(1000, 1000)

            segmentos.clear()

            puntos = 0
            delay = 0.1

            texto_puntos.clear()
            texto_puntos.write(f"Puntos: {puntos}  Máx Puntos: {max_puntos}", align="center", font=("Courier", 18, "normal"))

    time.sleep(delay)

ventana.mainloop()
