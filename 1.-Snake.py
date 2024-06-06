from cgitb import text
from tracemalloc import stop
import turtle
import time
import random

retraso = 0.1
marcador = 0
marcador_alto = 0

s = turtle.Screen()
serp = turtle.Turtle()
s.setup(650,650)
s.title("Serpiente")
s.bgcolor("grey")

serp.speed(1)
serp.shape("square")
serp.penup()
serp.goto(0,0)
serp.direction = "stop"
serp.color("blue")

comida = turtle.Turtle()
comida.shape("circle")
comida.color("orange")
comida.penup()
comida.goto(0,100)
comida.speed(0)

cuerpo = []

texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0,-260)
texto.write("Marcador: 0\t Marcador más alto: 0", align="center", font=("verdana", 24, "normal"))

def arriba():
    serp.direction = "up"
def abajo():
    serp.direction = "down"
def derecha():
    serp.direction = "right"
def izquierda():
    serp.direction = "left"

#Movimiento a la seerpiente
def movimiento():
    if serp.direction == "up":
        y = serp.ycor()
        serp.sety(y+20)
    if serp.direction == "down":
        y = serp.ycor()
        serp.sety(y-20)
    if serp.direction == "right":
        x = serp.xcor()
        serp.setx(x+20)
    if serp.direction == "left":
        x = serp.xcor()
        serp.setx(x-20)

s.listen()
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")

#ejecu del proy
while True:
    s.update()

    if serp.xcor() > 300 or serp.xcor() < -300 or serp.ycor() > 300 or serp.ycor() <-300:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serp.home()
        serp.direction = "stop"
        cuerpo.clear()
        
        marcador = 0
        texto.clear()
        texto.write("Marcador:{}\tMarcador más alto:{}".format(marcador,marcador_alto), align="center", font=("verdana", 24,"normal"))
    
    if serp.distance(comida) < 20:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        comida.goto(x,y)
        
        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("blue")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo)

        marcador +=10
        if marcador > marcador_alto:
            marcador_alto = marcador
            texto.clear()
            texto.write("Marcador:{}\tMarcador más alto:{}".format(marcador,marcador_alto), align="center", font=("verdana", 24,"normal"))

    total = len(cuerpo)
    for i in range(total -1,0,-1):
        x = cuerpo[i-1].xcor()
        y = cuerpo[i-1].ycor()
        cuerpo[i].goto(x,y)

    if total>0:
        x=serp.xcor()
        y=serp.ycor()
        cuerpo[0].goto(x,y)
        #pass


    movimiento()

    for i in cuerpo:
        if i.distance(serp) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serp.home()
            cuerpo.clear()
            serp.direction = "stop"

            marcador = 0
            texto.clear()
            texto.write("Marcador:{}\tMarcador más alto:{}".format(marcador,marcador_alto), align="center", font=("verdana", 24,"normal"))


    time.sleep(retraso)


turtle.done()