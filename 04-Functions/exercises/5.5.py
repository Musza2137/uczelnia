import figures
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
turtle.speed(5)

# Pierwszy zestaw figur (górna część ekranu)
turtle.penup()
turtle.goto(-200, 150)
turtle.pendown()
figures.draw_square(80)

turtle.penup()
turtle.goto(-50, 100)
turtle.pendown()
figures.draw_triangle(80)

turtle.penup()
turtle.goto(100, 150)
turtle.pendown()
figures.draw_rectangle(100, 50)

# Drugi zestaw figur (dolna część ekranu)
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
figures.draw_square(60)

turtle.penup()
turtle.goto(-50, -100)
turtle.pendown()
figures.draw_triangle(100)

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
figures.draw_rectangle(70, 110)

turtle.hideturtle()
window.mainloop()
