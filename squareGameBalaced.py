import turtle, random, time

score = 0
up = 0
down = 0
left = 0
right = 0

screen = turtle.Screen()
screen.tracer(0)
screen.setup(640, 640, 0, 0)
screen.bgcolor("#444444")

player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("lime")
player.pu()
player.goto(0, 0)
player.shapesize(2, 2, None)

enemy1 = turtle.Turtle()
enemy1.speed(0)
enemy1.shape("square")
enemy1.color("red")
enemy1.pu()
enemy1.goto(random.randint(-310, 310), random.randint(320, 960))

enemy2 = turtle.Turtle()
enemy2.speed(0)
enemy2.shape("square")
enemy2.color("red")
enemy2.pu()
enemy2.goto(random.randint(-310, 310), random.randint(320, 960))

enemy3 = turtle.Turtle()
enemy3.speed(0)
enemy3.shape("square")
enemy3.color("red")
enemy3.pu()
enemy3.goto(random.randint(-310, 310), random.randint(320, 960))

enemy4 = turtle.Turtle()
enemy4.speed(0)
enemy4.shape("square")
enemy4.color("red")
enemy4.pu()
enemy4.goto(random.randint(-310, 310), random.randint(320, 960))

enemy5 = turtle.Turtle()
enemy5.speed(0)
enemy5.shape("square")
enemy5.color("red")
enemy5.pu()
enemy5.goto(random.randint(-310, 310), random.randint(320, 960))

enemy6 = turtle.Turtle()
enemy6.speed(0)
enemy6.shape("square")
enemy6.color("red")
enemy6.pu()
enemy6.goto(random.randint(-310, 310), random.randint(320, 960))

enemy7 = turtle.Turtle()
enemy7.speed(0)
enemy7.shape("square")
enemy7.color("red")
enemy7.pu()
enemy7.goto(random.randint(-310, 310), random.randint(320, 960))

enemy8 = turtle.Turtle()
enemy8.speed(0)
enemy8.shape("square")
enemy8.color("red")
enemy8.pu()
enemy8.goto(random.randint(-310, 310), random.randint(320, 960))

enemy9 = turtle.Turtle()
enemy9.speed(0)
enemy9.shape("square")
enemy9.color("red")
enemy9.pu()
enemy9.goto(random.randint(-310, 310), random.randint(320, 960))

enemy0 = turtle.Turtle()
enemy0.speed(0)
enemy0.shape("square")
enemy0.color("red")
enemy0.pu()
enemy0.goto(random.randint(-310, 310), random.randint(320, 960))

def moveEnemiesDown(amount):
    enemy1.goto(enemy1.xcor(),enemy1.ycor() - amount)
    enemy2.goto(enemy2.xcor(),enemy2.ycor() - amount)
    enemy3.goto(enemy3.xcor(),enemy3.ycor() - amount)
    enemy4.goto(enemy4.xcor(),enemy4.ycor() - amount)
    enemy5.goto(enemy5.xcor(),enemy5.ycor() - amount)
    enemy6.goto(enemy6.xcor(),enemy6.ycor() - amount)
    enemy7.goto(enemy7.xcor(),enemy7.ycor() - amount)
    enemy8.goto(enemy8.xcor(),enemy8.ycor() - amount)
    enemy9.goto(enemy9.xcor(),enemy9.ycor() - amount)
    enemy0.goto(enemy0.xcor(),enemy0.ycor() - amount)

def checkForMoveUp():
    global score
    if enemy1.ycor() <= -330:
        enemy1.goto(random.randint(-310, 310), random.randint(330, 400))
        score += 1
    if enemy2.ycor() <= -330:
        enemy2.goto(random.randint(-310, 310), random.randint(330, 400))
        score += 1
    if enemy3.ycor() <= -330:
        enemy3.goto(random.randint(-310, 310), random.randint(330, 400))
        score += 1
    if enemy4.ycor() <= -330:
        enemy4.goto(random.randint(-310, 310), random.randint(330, 400))
        score += 1
    if enemy5.ycor() <= -330:
        enemy5.goto(random.randint(-310, 310), random.randint(330, 400))
        score += 1
    if enemy6.ycor() <= -330:
        enemy6.goto(random.randint(-310, 310), random.randint(330, 400))
        score += 1
    if enemy7.ycor() <= -330:
        enemy7.goto(random.randint(-310, 310), random.randint(330, 400))
        score += 1
    if enemy8.ycor() <= -330:
        enemy8.goto(random.randint(-310, 310), random.randint(330, 400))
        score += 1
    if enemy9.ycor() <= -330:
        enemy9.goto(random.randint(-310, 310), random.randint(330, 400))
        score += 1
    if enemy0.ycor() <= -330:
        enemy0.goto(random.randint(-310, 310), random.randint(330, 400))
        score += 1

def checkForCollision():
    global player
    if (player.xcor() - enemy1.xcor()) >= -30 and (player.xcor() - enemy1.xcor()) <= 30 and (player.ycor() - enemy1.ycor()) >= -30 and (player.ycor() - enemy1.ycor()) <= 30:return True
    elif (player.xcor() - enemy2.xcor()) >= -30 and (player.xcor() - enemy2.xcor()) <= 30 and (player.ycor() - enemy2.ycor()) >= -30 and (player.ycor() - enemy2.ycor()) <= 30:return 1
    elif (player.xcor() - enemy3.xcor()) >= -30 and (player.xcor() - enemy3.xcor()) <= 30 and (player.ycor() - enemy3.ycor()) >= -30 and (player.ycor() - enemy3.ycor()) <= 30:return 1
    elif (player.xcor() - enemy4.xcor()) >= -30 and (player.xcor() - enemy4.xcor()) <= 30 and (player.ycor() - enemy4.ycor()) >= -30 and (player.ycor() - enemy4.ycor()) <= 30:return 1
    elif (player.xcor() - enemy5.xcor()) >= -30 and (player.xcor() - enemy5.xcor()) <= 30 and (player.ycor() - enemy5.ycor()) >= -30 and (player.ycor() - enemy5.ycor()) <= 30:return 1
    elif (player.xcor() - enemy6.xcor()) >= -30 and (player.xcor() - enemy6.xcor()) <= 30 and (player.ycor() - enemy6.ycor()) >= -30 and (player.ycor() - enemy6.ycor()) <= 30:return 1
    elif (player.xcor() - enemy7.xcor()) >= -30 and (player.xcor() - enemy7.xcor()) <= 30 and (player.ycor() - enemy7.ycor()) >= -30 and (player.ycor() - enemy7.ycor()) <= 30:return 1
    elif (player.xcor() - enemy8.xcor()) >= -30 and (player.xcor() - enemy8.xcor()) <= 30 and (player.ycor() - enemy8.ycor()) >= -30 and (player.ycor() - enemy8.ycor()) <= 30:return 1
    elif (player.xcor() - enemy9.xcor()) >= -30 and (player.xcor() - enemy9.xcor()) <= 30 and (player.ycor() - enemy9.ycor()) >= -30 and (player.ycor() - enemy9.ycor()) <= 30:return 1
    elif (player.xcor() - enemy0.xcor()) >= -30 and (player.xcor() - enemy0.xcor()) <= 30 and (player.ycor() - enemy0.ycor()) >= -30 and (player.ycor() - enemy0.ycor()) <= 30:return 1
    else:return 0

def playerMovement(speed):
    global up, down, left, right
    if up == 1:player.goto(player.xcor() + speed, player.ycor())
    if down == 1:player.goto(player.xcor() - speed, player.ycor())
    if left == 1:player.goto(player.xcor(), player.ycor() - speed)
    if right == 1:player.goto(player.xcor(), player.ycor() + speed)
    if player.xcor() > 300:player.goto(300, player.ycor())
    if player.xcor() < -300:player.goto(-300, player.ycor())
    if player.ycor() > 300:player.goto(player.xcor(), 300)
    if player.ycor() < -300:player.goto(player.xcor(), -300)

def playerRight():
    global up
    up = 1
def playerLeft():
    global down
    down = 1
def playerDown():
    global left
    left = 1
def playerUp():
    global right
    right = 1

def playerRightR():
    global up
    up = 0
def playerLeftR():
    global down
    down = 0
def playerDownR():
    global left
    left = 0
def playerUpR():
    global right
    right = 0

def die():
    screen.bye()

screen.onkeypress(playerUp, "w")
screen.onkeypress(playerLeft, "a")
screen.onkeypress(playerDown, "s")
screen.onkeypress(playerRight, "d")

screen.onkeyrelease(playerUpR, "w")
screen.onkeyrelease(playerLeftR, "a")
screen.onkeyrelease(playerDownR, "s")
screen.onkeyrelease(playerRightR, "d")

screen.onkeypress(playerUp, "Up")
screen.onkeypress(playerLeft, "Left")
screen.onkeypress(playerDown, "Down")
screen.onkeypress(playerRight, "Right")

screen.onkeyrelease(playerUpR, "Up")
screen.onkeyrelease(playerLeftR, "Left")
screen.onkeyrelease(playerDownR, "Down")
screen.onkeyrelease(playerRightR, "Right")

screen.listen()
h = False

z = 10
while True:
    moveEnemiesDown(round(z))
    checkForMoveUp()
    playerMovement(round(z / 2) + 5)
    h = checkForCollision()
    if h == 1:
        break
    screen.update()
    time.sleep(1 / 60)
    z += 0.01

enemy1.hideturtle()
enemy2.hideturtle()
enemy3.hideturtle()
enemy4.hideturtle()
enemy5.hideturtle()
enemy6.hideturtle()
enemy7.hideturtle()
enemy8.hideturtle()
enemy9.hideturtle()
enemy0.hideturtle()
player.hideturtle()

player.goto(0,0)
player.color("#ffffff")
t = "Game Over!! Score: " + str(score) + "!"
player.write(t, align = "center", font = ["Arial", 30, "normal"])

screen.onkey(die, "space")

screen.update()
screen.mainloop()