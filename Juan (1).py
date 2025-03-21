from turtle import *
import colorsys
import random
import time

# Configuración de la pantalla
screen = Screen()
screen.setup(width=800, height=800)
screen.title("Feliz día mi reina")
screen.bgcolor("skyblue")  # Fondo azul cielo

# Dibujar nubes grandes, bonitas y separadas
def dibujar_nube(x, y, tamaño):
    penup()
    goto(x, y)
    pendown()
    color("white")
    begin_fill()
    for _ in range(6):
        circle(tamaño, 90)
        rt(120)
        circle(tamaño, 90)
    end_fill()

# Dibujar nubes rápidamente y separadas
speed(0)  # Velocidad máxima para las nubes
nube_posiciones = [(-250, 250), (-100, 200), (150, 220), (300, 180), (-300, 100), (250, 130)]
for x, y in nube_posiciones:
    tamaño = random.randint(40, 60)
    dibujar_nube(x, y, tamaño)

# Dibujar el tallo verde del girasol
speed(10)  # Velocidad rápida para el tallo
h = 0
penup()
goto(0, -100)
pendown()
color("green")
begin_fill()
rt(90)
fd(400)
lt(90)
fd(20)
lt(90)
fd(400)
lt(90)
fd(20)
end_fill()

# Dibujar el girasol con velocidad súper rápida
speed(0)  # Velocidad máxima para la flor
penup()
goto(0, 0)
pendown()
for i in range(16):
    for j in range(18):
        color("yellow")  # Todos los pétalos son amarillos
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)

# Colorear el centro de marrón
penup()
goto(-20, 0)
pendown()
color("brown")
begin_fill()
circle(44)  # Ajustar el radio del centro
end_fill()

# Mostrar el texto en la parte inferior
penup()
goto(0, -250)  # Posición debajo de la flor
pendown()
color("orange")
write("Feliz día mi reina", align="center", font=("Arial", 18, "bold"))

# Dibujar el pasto después de la flor
def dibujar_pasto():
    penup()
    goto(-400, -300)
    pendown()
    color("green")
    begin_fill()
    for _ in range(2):
        fd(800)
        rt(90)
        fd(100)
        rt(90)
    end_fill()
    
done()

