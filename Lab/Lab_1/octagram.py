from turtle import *

# edge_length = 100
# angle = 45
# vertices = []

# def draw_triangle(i, colour):
#     home()
#     right((i + 0.5) * angle)
#     forward(180)
#     pendown()
#     color(colour)    
#     begin_fill()
#     goto(vertices[i])
#     goto(vertices[i + 1])
#     end_fill()
#     penup()


# left(angle/2)
# forward(80)
# vertices.append(pos())
# for _ in range(7):
# 	left(angle)
# 	forward(80)
# 	vertices.append(pos())
# vertices.append(vertices[0])

# color('yellow')
# begin_fill()
# for v in vertices:
# 	goto(v)
# end_fill()
# penup()
# for i in range(4):
# 	draw_triangle(2 * i ,'blue')
# 	draw_triangle(2 * i + 1 ,'red')


small_edge_length = 100
long_edge_length = 180
angle = 45


def draw_triangle(i, colour):
    home()
    right((i + 0.5) * angle)
    forward(long_edge_length)
    pendown()
    color(colour)    
    begin_fill()
    goto(vertices[i])
    goto(vertices[i + 1])
    end_fill()
    # penup()


vertices = []
# penup()
for i in range(8):
    right(i * angle)
    forward(small_edge_length)
    vertices.append(pos())
    home()
vertices.append(vertices[0])
pendown()
color('yellow')
begin_fill()
for v in vertices:
    goto(v)
end_fill()
# penup()
for i in range(4):
    draw_triangle(2 * i, 'blue')
    draw_triangle(2 * i + 1, 'red')