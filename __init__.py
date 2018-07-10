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
# To move player left and right
playerspeed = 15

#Enemy player
enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)
enemySpeed = 2


#Player bullet
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletspeed = 20
#Bullet State:
#ready - ready to fire
bulletstate = ready
#fire - bullet is firing


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

def fire_bullet():
    # Declare bulletstate as a global if it needs to be changed
    # Global variables can be accesed anywhere in the skript
    # It should be global because, it will allow us to make direct changed that reflet the varable (wherever it is)
    global bulletstate

    # Move the bullet above the player
    x = player.xcor()
    y = player.ycor()
    bullet.setposition(x, y+10)
    bullet.showturtle()

# activates the left and right functions
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

# Main game mainloop
while True:
    #Move the enemy
    x = enemy.xcor()
    x += enemySpeed
    enemy.setx(x)

    #Keeps the enemy in the border and moves it doen when it tuches a border
    if (enemy.xcor() > 285):
        y = enemy.ycor()
        y -= 40
        enemySpeed *= -1
        enemy.sety(y)

    if (enemy.xcor() < -285):
        y = enemy.ycor()
        y -= 40
        enemySpeed *= -1
        enemy.sety(y)

#Creates a delay so that the turtle window does not disappear
delay = input("Press enter to finish.")
# turtle.mainloop()
