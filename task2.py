import turtle
import math


def draw_pythagoras_tree(t, length, angle, depth):
    if depth == 0:
        return

    t.forward(length)
    
    t.left(angle)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, angle, depth - 1)
    
    t.right(2 * angle)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, angle, depth - 1)
    
    t.left(angle)
    t.backward(length)

depth = int(input("Введіть рівень рекурсії для дерева Піфагора: "))

screen = turtle.Screen()
screen.title("Дерево Піфагора")
screen.setup(width=800, height=800)


t = turtle.Turtle()
t.speed(10000000)
t.left(90)  
t.hideturtle()

initial_length = 100  
angle = 45 

draw_pythagoras_tree(t, initial_length, angle, depth)

turtle.done()