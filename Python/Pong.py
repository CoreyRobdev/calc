import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# stops window from updating
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
# 'turtle' is the module name. 'Turtle' is the class name.
paddle_a = turtle.Turtle()

# sets speed to max, shape to square, and color to white
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# 'penup' prevents moving pixels from leaving a trace
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# 'd' meaning 'delta' or a change in 2 values
ball.dx = .138
ball.dy = -.138

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player1: 0 Player2: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up():
 # Grabs the Y coordinates from paddle_a, moves up 20 pixels, then sets Y coordinates
 y = paddle_a.ycor()
 y += 20
 paddle_a.sety(y)

def paddle_a_down():
 y = paddle_a.ycor()
 y -= 20
 paddle_a.sety(y)

def paddle_b_up():
 y = paddle_b.ycor()
 y += 20
 paddle_b.sety(y)

def paddle_b_down():
 y = paddle_b.ycor()
 y -= 20
 paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
 wn.update()

 # Move Ball
 ball.setx(ball.xcor() + ball.dx)
 ball.sety(ball.ycor() + ball.dy)

 # Border check 
 if ball.ycor() > 290:
  ball.sety(290)
  ball.dy *= -1
  winsound.PlaySound("C:/Users/kingc/Documents/websites/Python/py-wall_bounce.wav", winsound.SND_ASYNC)

 if ball.ycor() < -290:
  ball.sety(-290)
  ball.dy *= -1
  winsound.PlaySound("C:/Users/kingc/Documents/websites/Python/py-wall_bounce.wav", winsound.SND_ASYNC)

 if ball.xcor() > 390:
  score_a += 1
  ball.goto(0, 0)
  ball.dx *= -1
  pen.clear()
  pen.write("Player1: {} Player2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
 
 if ball.xcor() < -390:
  score_b += 1
  ball.goto(0, 0)
  ball.dx *= -1
  pen.clear()
  pen.write("Player1: {} Player2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

 # Paddle and Ball collisions
 if ball.xcor() > 340 and ball.xcor() < 350 and(ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
  ball.setx(340)
  ball.dx *= -1
  winsound.PlaySound("C:/Users/kingc/Documents/websites/Python/py-a_bounce.wav", winsound.SND_ASYNC)

 if ball.xcor() < -340 and ball.xcor() > -350 and(ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
  ball.setx(-340)
  ball.dx *= -1
  winsound.PlaySound("C:/Users/kingc/Documents/websites/Python/py-a_bounce.wav", winsound.SND_ASYNC)