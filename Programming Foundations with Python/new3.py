import turtle

def draw_square(some_turtle):
    for _ in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for _ in range(3):
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    john = turtle.Turtle()

    for _ in range(36):
        draw_triangle(john)
        john.right(10)
    john.forward(200)
    

    window.exitonclick()
    
draw_art()
