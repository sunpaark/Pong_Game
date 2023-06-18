import turtle

#Creating background
root = turtle.Screen()
root.title("Let's Play Pong!")
root.bgcolor("black")
root.setup(width = 1000, height = 600)
#Stops the program to auto-update, which speeds up the game a bit.
root.tracer(0)

#Creating left paddle
lstick = turtle.Turtle()
#Not the speed of the paddle actually moving. The speed of the paddle's animation.
lstick.speed(0)
lstick.shape("square")
lstick.color("white")
lstick.shapesize(stretch_wid = 3, stretch_len = 1)
#Demanding the program to not draw lines when the paddle is moving.
lstick.penup()
lstick.goto(-400, 0)

#Creating right paddle
rstick = turtle.Turtle()
rstick.speed(0)
rstick.shape("square")
rstick.color("white")
rstick.shapesize(stretch_wid = 3, stretch_len = 1)
rstick.penup()
rstick.goto(400, 0)

#creating the ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
#Ball moving in x direction by positive 2 pixels
ball.dx = 0.5
#Ball moving in y direction by positive 2 pixels
ball.dy = 0.5

#Initializing the score
player1 = 0
player2 = 0

#Displaying the score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player_1 : 0 Player_2 : 0", align = "center", font = ("Calibri", 24, "normal"))

#Allowing the player to move the paddle vertically (The function)
def lstickup():
    #Gets the current y-coordinate of the left paddle.
    y = lstick.ycor()
    #Adding or subtracting y by 20. Actually, allowing the paddle to move because the value of the coordinate is de/increasing.
    y += 20
    #Assigning that 
    lstick.sety(y)
    
def lstickdown():
    y = lstick.ycor()
    y -= 20
    lstick.sety(y)
    
def rstickup():
    y = rstick.ycor()
    y += 20
    rstick.sety(y)
    
def rstickdown():
    y = rstick.ycor()
    y -= 20
    rstick.sety(y)
    
#Keyboard Settings
#Tells the program to "listen" to the keyboard input
root.listen()
root.onkeypress(lstickup, "w")
root.onkeypress(lstickdown, "s")
root.onkeypress(rstickup, "Up")
root.onkeypress(rstickdown, "Down")

#Main game loop
while True:
    root.update()
    
    #Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Creating boarders
    if ball.ycor() > 280:
        ball.sety(280)
        #Reverse the direction
        ball.dy *= -1
        
    if ball.ycor() < -280:
       ball.sety(-280)
       ball.dy *= -1
       
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dy *= -1
        player1 += 1
        score.clear()
        score.write("Player 1 : {}      Player 2 : {}". format(player1, player2), align = "center", font = ("Calibri", 24, "normal"))
        
    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dy *= -1
        player2 += 1
        score.clear()
        score.write("Player 1 : {}      Player 2 : {}". format(player1, player2), align = "center", font = ("Calibri", 24, "normal"))
        
    if lstick.ycor() > 280:
        lstick.sety(280)
        lstick.ycor
        
    #Paddle and Ball Collision
    if (ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < lstick.ycor() + 40 and ball.ycor() > lstick.ycor() -40): 
        ball.setx(-360) 
        ball.dx *= -1
        
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < rstick.ycor() + 40 and ball.ycor() > rstick.ycor() -40): 
            ball.setx(360) 
            ball.dx *= -1