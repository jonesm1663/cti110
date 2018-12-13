 import turtle

"""This teaches our program how to make triangles
of a color and x,y coordinates we choose
"""
def make_triangle(x, y, color):
  turtle.penup()
  turtle.goto(x,y)
  turtle.begin_fill()
  turtle.color(color)
  turtle.pendown()
  for count in range(3):
    turtle.forward(50)
    turtle.left(120)
  turtle.end_fill()

"""This teaches our program how to make triangles of a color and x,y squares we choose
"""
def make_square(x, y, color):
  turtle.penup()
  turtle.goto(x,y)
  turtle.begin_fill()
  turtle.color(color)
  turtle.pendown()
  for count2 in range(3):
    turtle.forward(50)
    turtle.left(90)
  turtle.end_fill()


turtle.shape("turtle")
turtle.penup()
turtle.goto(0,-150)
turtle.color('#999999')
turtle.begin_fill()
turtle.pendown()
turtle.circle(150)
turtle.penup()
turtle.end_fill()
turtle.left(180)
# The Teeth:
make_triangle(60, -20, '#ffff66')
make_triangle(10, 15, '#3333ff')
make_triangle(-60, -20, '#ffff00')
turtle.left(180)

# The Eyes:
make_triangle(-70, 50, '#ff0000')
make_triangle(20, 50, '#ff0000')

# The Stump:
make_square(-15, -100, '#000000')
turtle.penup()
turtle.goto(-100,-185)
turtle.write('Happy Halloween Mike!', None, None, "20pt normal")
turtle.goto(-120,-185)
turtle.left(180)
