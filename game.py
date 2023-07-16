# import turtle module
import random
import turtle

#------ Create and set window --------
window = turtle.Screen()
window.title("Ping Pong Game")              # name of the screen
window.bgcolor("black")                     # set the background color of the screen
window.setup(height=600 , width = 800)      # Set the size and position of the main window
window.tracer(0)                            # Turns turtle animation off (no update)

# create Player 1
player1 = turtle.Turtle()
player1.speed(0)                                  # set the turtle's speed
player1.shape("square")                           # Set player shape
player1.color("red")                              # set the pencolor and fillcolor.
player1.penup()                                   # -- no drawing when moving.
player1.shapesize(stretch_wid=5,stretch_len=1)  # set player dimensions
player1.goto(-380,0)                              # Move player to an absolute position.

# create Player 2
player2 = turtle.Turtle()
player2.speed(0)                                  # set the turtle's speed
player2.shape("square")                           # Set player shape
player2.color("blue")                             # set the pencolor and fillcolor.
player2.penup()                                   # -- no drawing when moving.
player2.shapesize(stretch_wid=5,stretch_len=1)  # set player dimensions
player2.goto(380,0)                               # Move player to an absolute position.

# Create ball
ball = turtle.Turtle()
ball.speed(0)                                  # set the ball updating speed
ball.shape("circle")                           # Set ball shape
ball.color("white")                            # set the pencolor and fillcolor.
ball.penup()                                   # -- no drawing when moving.
ball.goto(0,0)                                 # Move ball to an absolute position.
random_list = [1,2,3,4,5,6,7,8,9,10]
x = int(random.choice(random_list))
y = int(random.choice(random_list))
if x >= 5 :
    ball.dx = 0.1
else:
    ball.dx = -0.1	
if y >= 5:                          
    ball.dy = 0.1
else:
    ball.dy = -0.1	

# score
scoreRed = 0
score1 = turtle.Turtle()
score1.speed(0)
score1.color("red")
score1.penup()
score1.hideturtle()
score1.goto(-150,260)
score1.write("Red Player: 0", align= "center", font=("Courier",20,"normal"))

scoreBlue = 0
score2 = turtle.Turtle()
score2.speed(0)
score2.color("blue")
score2.penup()
score2.hideturtle()
score2.goto(150,260)
score2.write("Blue Player: 0", align= "center", font=("Courier",20,"normal"))

#------ Functions -------

# function to move player1 up
def player1_up():
    y = player1.ycor()                         # get the player's1 y coordinate
    if y<=240:
        y += 20
        player1.sety(y)

# function to move player1 down
def player1_down():
    y = player1.ycor()
    if y>=-230:
        y -= 20
        player1.sety(y)

# function to move player2 up
def player2_up():
    y = player2.ycor()
    if y<=240:
        y += 20
        player2.sety(y)

# function to move player2 down
def player2_down():
    y = player2.ycor()
    if y>=-230:
        y -= 20
        player2.sety(y)


#------keybords bindings---------
window.listen()
window.onkeypress(player1_up,"w")
window.onkeypress(player1_down,"s")

window.onkeypress(player2_up,"Up")
window.onkeypress(player2_down,"Down")


#------ Create the main loop for the game --------
while True:
    window.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # when the ball hit up border
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1
    
    # when the ball hit down border
    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1
    
    # when the ball hit right border
    if ball.xcor() > 385 :
        ball.goto(0,0)
        ball.dx *= -1
        scoreRed += 1
        score1.clear()
        score1.write("Red Player: {}".format(scoreRed), align= "center", font=("Courier",20,"normal"))

    # when the ball hit left border
    if ball.xcor() < -385 :
        ball.goto(0,0)
        ball.dx *= -1
        scoreBlue += 1
        score2.clear()
        score2.write("Blue Player: {}".format(scoreBlue), align= "center", font=("Courier",20,"normal"))
    # when the player hit the ball
    if (ball.xcor() > 370 and ball.xcor() < 380) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() -40):
        ball.setx(370)
        ball.dx *= -1

    if (ball.xcor() < -370 and ball.xcor() > -380) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() -40):
        ball.setx(-370)
        ball.dx *= -1