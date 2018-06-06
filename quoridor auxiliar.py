import turtle

def drawBoardSqr(t):
    t.color("sienna")
    t.fillcolor("sienna")
    t.begin_fill()
    for i in range(4):
        t.fd(30)
        t.left(90)
    t.end_fill()

def drawSqrRow(t):
    for i in range(9):
        t.down()
        drawBoardSqr(t)
        t.up()
        t.fd(50)

def drawBoard(t1,t2):
    t1.setposition(-215,-215)
    t2.setposition(-215,-165)
    t1.up()
    t2.up()
    t1.speed(0)
    t2.speed(0)
    drawSqrRow(t1), drawSqrRow(t2)


wn = turtle.Screen()
wn.bgcolor("DarkSalmon")

drawer1= turtle.Turtle()
drawer2= turtle.Turtle()
drawer3= turtle.Turtle()
drawer4= turtle.Turtle()
drawer5= turtle.Turtle()
drawer6= turtle.Turtle()
drawer7= turtle.Turtle()
drawer8= turtle.Turtle()
drawer9= turtle.Turtle()

BoardDrawingTeam = (drawer1, drawer2, drawer3, drawer4, drawer5, drawer6, drawer7, drawer8, drawer9)
testcouple = (drawer1, drawer2)
drawBoard(drawer1, drawer2)

