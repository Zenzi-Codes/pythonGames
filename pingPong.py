# learning through freeCodeCamp.org course on youtube
# https://www.youtube.com/watch?v=XGfGcyHPhc&feature=youtu.be

import turtle
import winsound

app = turtle.Screen()
app.title("Zenzi-Pong")
app.bgcolor("#2c2925")
app.setup(width=800, height=600)
app.tracer(0)

# score

score = 0

# Paddle left

paddle_a = turtle.Turtle()
paddle_a.speed(0) # animation speed not paddle speed
paddle_a.shape("square")
paddle_a. shapesize(stretch_wid= 5, stretch_len=1) # making paddle rectangle
paddle_a.color("#e6b1bd")
paddle_a.penup()
paddle_a.goto(-350, 0) # start position of paddle

# Paddle right

paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b. shapesize(stretch_wid= 5, stretch_len=1)
paddle_b.color("#d53a44")
paddle_b.penup()
paddle_b.goto(350, 0) 

# Ping Pong ball

ball = turtle.Turtle()
ball.speed(0) 
ball.shape("circle")
ball.color("#faf2f2")
ball.penup()
ball.goto(0, 0) # start position of ball

# ball movement
ball.dx = 1
ball.dy = 0.6

# score display

score_board = turtle.Turtle()
score_board.speed(0)
score_board.color("#ae4044")
score_board.penup()
score_board.hideturtle()
score_board.goto(160, 260)
score_board.write("Score: {}".format(score), align="center", font=("Courier", 21, "normal"))

# Functions

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 # moves paddle up 20px
    paddle_a.sety(y)

def paddle_a_dwn():
    y = paddle_a.ycor()
    y -= 20 # moves paddle down 20px
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20 # moves paddle up 20px
    paddle_b.sety(y)

def paddle_b_dwn():
    y = paddle_b.ycor()
    y -= 20 # moves paddle down 20px
    paddle_b.sety(y)

# Keyboard binding

app.listen()
app.onkeypress(paddle_b_up, "Up")
app.onkeypress(paddle_b_dwn, "Down")

# main loop

while True:
    app.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    #    winsound.PlaySound("#", winsound.SND_ASYNC) # add bounce sound
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
   #     winsound.PlaySound("#", winsound.SND_ASYNC) # add bounce sound

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # collision detection
    
    # right paddle collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        score_board.clear()
        score += 5
        score_board.write("Score: {}".format(score), align="center", font=("Courier", 21, "normal"))
  #      winsound.PlaySound("#", winsound.SND_ASYNC) # add collision sound

    # left paddle collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
 #       winsound.PlaySound("#", winsound.SND_ASYNC) # add collision sound

    # left paddle chases ball
    if (ball.ycor() - paddle_a.ycor() >= 15) and (ball.xcor() < 300):
        paddle_a_up()
    
    if (ball.ycor() - paddle_a.ycor() <= -15) and (ball.xcor() < 300):
        paddle_a_dwn()

    # ball changes gets faster as you play
    ball.dx *= 1.00003
