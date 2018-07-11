# Set up the screen
import turtle
import os
import math
import random

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

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

#set score to zero
score = 0

#Draw the Score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("White")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = "left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

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

#Choose the number of enemies
number_of_enemis = 5
#Create an empty list of enemies
enemies = []
#Add enemies to the list
for i in range(number_of_enemis):
    #Create enemy players
    enemies.append(turtle.Turtle())

#Give Each enemy a feature

for enemy in enemies:
    enemy.color('red')
    enemy.shape('circle')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)
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
#fire - bullet is firing
bulletstate = "ready"

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

    if(bulletstate == "ready"):
        bulletstate = "fire"
        # Move the bullet above the player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y+10)
        bullet.showturtle()

#Check if the bullet and the enemy have touched
def isCollition(t1, t2):
    distance = math.sqrt(math.pow((t2.xcor() - t1.xcor()),2) + math.pow((t2.ycor() - t1.ycor()), 2))
    if(distance < 25):
        return True
    else:
        return False

# activates the left and right functions
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")
# Main game mainloop
while True:

    for enemy in enemies:
        #Move the enemy
        enemyx = enemy.xcor()
        enemyx += enemySpeed
        enemy.setx(enemyx)

        #Keeps the enemies in the border and moves them down when one of them touches a border
        if (enemy.xcor() > 285):
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemySpeed *= -1
        if (enemy.xcor() < -285):
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemySpeed *= -1

        #Check collition between the bullet and the enemy
        if(bulletstate == "fire"):
            if isCollition(enemy, bullet):
                #reset the bullet
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0, -400)

                #reset the enemy
                x = random.randint(-200, 200)
                y = random.randint(100, 250)
                enemy.setposition(x, y)

                #Update the score
                score += 10
                scorestring = "Score: %s" %score
                score_pen.clear()
                score_pen.write(scorestring, False, align = "left", font=("Arial", 14, "normal"))

        #Check collition between the player and the enemy
        if isCollition(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            bullet.hideturtle()
            print("GAME OVER!")
            break

    #For the Bullet:
    if(bulletstate == "fire"):
        # Move the bullet
        bullety = bullet.ycor()
        bullety += bulletspeed
        bullet.sety(bullety)

    # Check to see if the bullet has gone out of bound
    if(bullet.ycor() > 275):
        bullet.hideturtle()
        bulletstate = "ready"

#Creates a delay so that the turtle window does not disappear
delay = input("Press enter to finish.")
# turtle.mainloop()
