# snake game
import turtle
import random
import time
delay = 0.1
score = 0
highestscore = 0
# snake body
bodies = []
# screen settings
s = turtle.Screen()
s.title = ("SNAKE GAME")
s.bgcolor = ("Black")
s.setup(width=800, height=800)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("pink")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("green")
food.fillcolor("yellow")
food.penup()
food.ht()  # hide turtle
food.goto(0, 300)
food.st()  # show turtle

# score board
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-300, 300)
sb.write("Score: 0 | Highest score: 0")


def moveup():
    if head.direction != "down":
        head.direction = "up"


def movedown():
    if head.direction != "up":
        head.direction = "down"


def moveleft():
    if head.direction != "right":
        head.direction = "left"


def moveright():
    if head.direction != "left":
        head.direction = "right"


def movestop():
    head.direction = "stop"


def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)


# key bindings
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")

# main loop
while True:
    s.update()
    # movement
    if head.xcor() > 390:
        head.setx(-390)
    if head.xcor() < -390:
        head.setx(390)
    if head.ycor() > 390:
        head.sety(-390)
    if head.xcor() < -390:
        head.setx(390)
    # collision with food
    if head.distance(food) < 20:
        # move the food to new random places
        x = random.randint(-390, 390)
        y = random.randint(-390, 390)
        food.goto(x, y)

        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        body.fillcolor("white")
        bodies.append(body)  # append new body
        # score update
        score = score+10
        # delay
        delay -= 0.001  # to increase the movement speed of snake
        # updating the highest score
        if score > highestscore:
            highestscore = score
        sb.clear()
        sb.write("Score: {} High score: {}".format(score, highestscore))
    # moving the snake body
    for index in range(len(bodies)-1, 0, -1):
        x = bodies[index-1].xcor()
        y = bodies[index-1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)
    move()

    # checking collision with body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for body in bodies:
                body.ht()
            bodies.clear()

            score = 0
            delay = 0.1
            # clearing up the score board
            sb.clear()
            sb.write("Score: {} highest score: {}".format(score, highestscore))
    time.sleep(delay)
s.mainloop()
# ggs wp ezz clap
