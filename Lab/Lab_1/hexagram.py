from turtle import *

edge_length = 150
angle = 120

def draw_triangle(colour):
    color(colour)
    for _ in range(3):
        forward(edge_length // 3)
        penup()
        forward(edge_length // 3)
        pendown()
        forward(edge_length // 3)
        left(angle)

penup()
forward(- edge_length // 2)
pendown()
draw_triangle('red')
penup()
forward(edge_length // 3 )
left(angle)
forward((edge_length // 3)*2)
left(180)
pendown()
draw_triangle('blue')
