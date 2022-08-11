import turtle, random, time

closed = 0
score = -10

class Enemy:
    def __init__(self, screenSize, speed):
        self.screenSize = screenSize
        self.halfSize = screenSize/2
        self.size = 0
        self.speed = speed
        self.enemy = turtle.Turtle()

    def reset(self):
        self.enemy.speed(0)
        self.enemy.shape("square")
        self.enemy.color("red")
        self.enemy.pu()
        self.enemy.hideturtle()
        self.moveToTop()

    def moveToTop(self):
        self.size = random.randint(10, 30)
        self.enemy.goto(random.randint(-self.halfSize + self.size, self.halfSize - self.size), random.randint(self.halfSize + self.size, self.halfSize*3))
        self.enemy.turtlesize(self.size / 10, self.size / 10)

    def show(self):
        self.enemy.showturtle()

    def move(self):
        self.enemy.goto(self.enemy.xcor(),self.enemy.ycor() - self.speed)
        if self.enemy.ycor() <= -self.halfSize - self.size:
            self.moveToTop()
            return 1
        return 0

    def hit(self, player):
        if (player.xcor() - self.enemy.xcor()) >= -20 - (self.size) and (player.xcor() - self.enemy.xcor()) <= 20 + (self.size) and (player.ycor() - self.enemy.ycor()) >= -20 - (self.size) and (player.ycor() - self.enemy.ycor()) <= 20 + (self.size):
            return True
        return False

def reset():
    global left, right, up, down, h, z, score

    screen.onkey(None, "space")
    screen.onkey(None, "r")

    player.speed(0)
    player.shape("square")
    player.color("lime")
    player.pu()
    player.goto(0, 0)
    player.shapesize(2, 2, None)

    for enemy in enemies:
        enemy.reset()

    score = -10
    up = 0
    down = 0
    left = 0
    z = 10
    h = 0
    right = 0

def showTurtles():
    player.showturtle()
    player.clear()
    for enemy in enemies:
        enemy.show()

def moveEnemiesDown():
    global score
    for enemy in enemies:
        score += enemy.move()

def checkForCollision():
    for enemy in enemies:
        if enemy.hit(player):
            return True
    return False

def playerMovement(speed):
    global up, down, left, right
    if up == 1:player.goto(player.xcor() + speed, player.ycor())
    if down == 1:player.goto(player.xcor() - speed, player.ycor())
    if left == 1:player.goto(player.xcor(), player.ycor() - speed)
    if right == 1:player.goto(player.xcor(), player.ycor() + speed)
    if player.xcor() > 290:player.goto(290, player.ycor())
    if player.xcor() < -300:player.goto(-300, player.ycor())
    if player.ycor() > 300:player.goto(player.xcor(), 300)
    if player.ycor() < -290:player.goto(player.xcor(), -290)

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
    global closed
    closed = 1
    screen.bye()

def death():
    for enemy in enemies:
        enemy.reset()

    player.hideturtle()

    player.goto(0,0)
    player.color("#ffffff")
    t = "Game Over!! Score: " + str(score) + "!"
    player.write(t, align = "center", font = ["Arial", 30, "normal"])

    screen.onkey(die, "space")
    screen.onkey(reset, "r")

    screen.update()

player = turtle.Turtle()
enemies = []
for i in range(10):
    enemies.append(Enemy(640, 10))

screen = turtle.Screen()
screen.tracer(0)
screen.setup(640, 640, 0, 0)
screen.bgcolor("#444444")

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

while True:
    reset()
    while h == False:
        showTurtles()
        moveEnemiesDown()
        playerMovement(round(z / 2) + 5)
        h = checkForCollision()
        if h == True:
            death()
        screen.update()
        time.sleep(1 / 60)
        z += 0.01
    while h == 1:
        time.sleep(1 / 20)
        if closed == 1:
            break
        try:
            screen.update()
        except:
            pass
    if closed == 1:
        break
