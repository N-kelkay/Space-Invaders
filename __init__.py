# Set up the screen
import turtle
import os

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

#Enemy player
enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemySpeed = 2

# To move player left and right
playerspeed = 15

#Move player Left
def move_left():
    x = player.xcor()
    x -= playerspeed
    if(x <= -285):
        player.setx(-285)
    else:
        player.setx(x)

#Move player Right
def move_right():
    x = player.xcor()
    x += playerspeed
    if(x >= 285):
        player.setx(285)
    else:
        player.setx(x)

# activates the left and right functions
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

# Main game mainloop
while True:
    #Move the enemy
    x = enemy.xcor()
    x += enemySpeed
    if(x >= 285):
        enemy.setx(-285)
    elif(x <= -285):
        enemy.setx(285)
    else:
        enemy.setx(x)

    y = enemy.ycor()
    y -+ enemySpeed
    if (y >= 285):
        enemy.sety(-285)
    elif(y <= -285):
        enemy.hide()
    else:
        enemy.sety(x)

#Creates a delay so that the turtle window does not disappear
delay = input("Press enter to finish.")
# turtle.mainloop()
