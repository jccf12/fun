import turtle

def drawEdge():
    drawer.pensize(2)
    drawer.color("sienna")
    drawer.up()
    drawer.setposition(-235,-235)
    drawer.down()
    for i in range(4):
        drawer.fd(470)
        drawer.left(90)

def drawBoardSqr():
    drawer.fillcolor("sienna")
    drawer.begin_fill()
    for i in range(4):
        drawer.fd(30)
        drawer.left(90)
    drawer.end_fill()

def drawBoard():
    drawEdge()
    drawer.up()
    drawer.setposition(-215,-215)
    x = 8
    for i in range(8):
        for i in range(9):
            drawer.down()
            drawBoardSqr()
            drawer.up()
            drawer.fd(50)
        drawer.fd(-450)
        drawer.left(90)
        drawer.fd(30)
        drawer.right(90)
        drawer.fd(-40)
        text = str(x)
        x = x - 1
        drawer.write(text,font=("Times New Roman", 16, "normal"))
        drawer.fd(40)
        drawer.left(90)
        drawer.fd(20)
        drawer.right(90)
    for i in range(9):
            drawer.down()
            drawBoardSqr()
            drawer.up()
            drawer.fd(50)
    drawer.fd(-412)
    drawer.left(90)
    drawer.fd(60)
    drawer.right(90)
    for i in range(8):
        drawer.write(str(i+1), font=("Times New Roman", 16, "normal"))
        drawer.fd(50)
    drawer.goto(0,268)
    drawer.write("COLUMNS", align="center", font=("Times New Roman", 32, "normal"))
    drawer.goto(-272,-15)
    drawer.write("ROWS", align="right", font=("Times New Roman", 32, "normal"))
    drawer.ht()
    drawer.setposition(0,0)
    
def accomodatePlayers():
    P1.up()
    P2.up()
    P1.shape('turtle')
    P2.shape('turtle')
    P1.setposition(0,200)
    P2.setposition(0,-200)
    P1.seth(270)
    P2.seth(90)
    P2.color("white")

  

def movePiece(player):
    
    ok = False
    done = False
    while not ok:
        if player == P1:
            inst = input("PLAYER 1: Choose direction (f, b, l, r)")
        elif player == P2:
            inst = input("PLAYER 2: Choose direction (f, b, l, r)")

        pilar = int((250 + player.xcor()) / 50)
        fila = int((250 - player.ycor()) / 50)
        
        
        if inst == "f":
            
            if 270 == player.heading():
                if str(pilar)+ str(fila) not in markersh:
                    player.fd(50)
                    ok = True
                    done = True
                else:
                    player.fd(20)
                    player.fd(-20)
                    print("invalid movement (fence in front or player out of board)")
                    ok = True
                    
            elif 90 == player.heading():
                if str(pilar)+ str(fila-1) not in markersh:
                    player.fd(50)
                    ok = True
                    done = True
                else:
                    player.fd(20)
                    player.fd(-20)
                    print("invalid movement (fence in front or player out of board)")
                    ok = True
                
            

        elif inst == "b":

            if 270 == player.heading():
                if str(pilar)+ str(fila-1) not in markersh:
                    player.fd(-50)
                    done = True
                else:
                    player.fd(-20)
                    player.fd(20)
                    print("invalid movement (fence in front or player out of board)")
            elif 90 == player.heading():
                if str(pilar)+ str(fila) not in markersh:
                    player.fd(-50)
                    done = True
                else:
                    player.fd(-20)
                    player.fd(20)
                    print("invalid movement (fence in front or player out of board)")
     
            ok = True                
                                             
            
        elif inst == "l":
            
            if 270 == player.heading():
                if str(pilar-1)+ str(fila) not in markersv:
                    player.right(90)
                    player.fd(50)
                    player.left(90)
                    done = True
                else:
                    player.right(90)
                    player.fd(20)
                    player.fd(-20)
                    player.left(90)
                    print("invalid movement (fence in front or player out of board)")

            elif 90 == player.heading():
                if str(pilar-1)+ str(fila) not in markersv:
                    player.left(90)
                    player.fd(50)
                    player.right(90)
                    done = True
                else:
                    player.left(90)
                    player.fd(20)
                    player.fd(-20)
                    player.right(90)
                    
                
            ok = True
            
        elif inst == "r":
            
            if 270 == player.heading():
                if str(pilar)+ str(fila) not in markersv:
                    player.left(90)
                    player.fd(50)
                    player.right(90)
                    done = True
                else:
                    player.left(90)
                    player.fd(20)
                    player.fd(-20)
                    player.right(90)
                
            elif 90 == player.heading():
                if str(pilar)+ str(fila) not in markersv:
                    player.right(90)
                    player.fd(50)
                    player.left(90)
                    done = True
                else:
                    player.right(90)
                    player.fd(20)
                    player.fd(-20)
                    player.left(90)
                    print("invalid movement (fence in front or player out of board)")
                    
            ok = True
            
        else:
            if player == P1:
                print('PLAYER 1: enter a valid instruction (f, b, l, r)')
            elif player == P2:
                print('PLAYER 2: enter a valid instruction (f, b, l, r)')

    return done
            

    
def placeFence(fence, orientation, col, row):
    
    fence.setposition(sfpx + 50*(col-1), sfpy - 50*(row-1))
    if orientation == "h":
        done = False
        if str(col)+str(row) not in markersh and str(col+1)+str(row) not in markersh and (str(col)+str(row) not in markersv or str(col)+str(row+1) not in markersv): 
            fence.fd(-35)
            fence.down()
            fence.fd(70)
            fence.up()
            fence.setposition(sfpx, sfpy)
            markersh.append(str(col)+str(row))
            markersh.append(str(col+1)+str(row))
            done = True
        else:
            print("Fence is in an invalid position, call your move again")
        


        
    elif orientation == "v":
        done = False
        while not done:
            if str(col)+str(row) not in markersv and str(col)+str(row+1) not in markersv and (str(col)+str(row) not in markersh or str(col+1)+str(row) not in markersh):
                fence.right(90)
                fence.fd(-35)
                fence.down()
                fence.fd(70)
                fence.up()
                fence.left(90)
                fence.setposition(sfpx, sfpy)
                markersv.append(str(col)+str(row))
                markersv.append(str(col)+str(row+1))
                done = True
            else:
                print("Fence is in an invalid position")
        
    return done           



def callMove(player, fence):
    ok = False
    doneplacingfence = False
    donemoving = False
    while not ok or not doneplacingfence or not donemoving:
        if player == P1:
            
            decision = input("PLAYER 1: Move or place fence? (m,f)")
            if decision == "m":
                
                donemoving = movePiece(player)
                ok = True
                doneplacingfence = True
                
            elif decision == "f":
                ok = True
                donemoving = True
                ok2 = False
                while not ok2:
                    orient = input("PLAYER 1: Choose orientation for fence (v,h)")
                    if orient == "v" or orient == "h":
                        ok2 = True
                    else:
                        print("PLAYER 1: enter valid input ('v' or 'h')")
                ok3 = False
                while not ok3:
                    col_str = input("PLAYER 1: Choose the column number for your fence")
                    if col_str in "12345678":
                        col_int = int(col_str)
                        if col_int < 9 and col_int > 0:
                            col = col_int
                            ok3 = True
                        else:
                            print("PLAYER 1: Please choose an integer bewteen 1 and 8, inclusive")
                    else:
                        print("PLAYER 1: Please choose an integer between 1 and 8, inclusive")
                ok4 = False
                while not ok4:
                    row_str = input("PLAYER 1: Choose the row number for your fence")
                    if row_str in "12345678":
                        row_int = int(row_str)
                        if row_int < 9 and row_int > 0:
                              row = row_int
                              ok4 = True
                        else:
                              print("PLAYER 1: please choose an integer between 1 and 8, inclusive")
                    else:
                        print("PLAYER 1: please choose an integer between 1 and 8, inclusive")
                
                doneplacingfence = placeFence(fence, orient, col, row)
            else:
                print("PLAYER 1: input not valid (type: 'm' or 'f')")

                
        elif player == P2:

            decision = input("PLAYER 2: Move or place fence? (m,f)")
            if decision == "m":
                donemoving = movePiece(player)
                ok = True
                doneplacingfence = True
                
            elif decision == "f":
                donemoving = True
                ok = True
                ok2 = False
                while not ok2:
                    orient = input("PLAYER 2: Choose orientation for fence (v,h)")
                    if orient == "v" or orient == "h":
                        ok2 = True
                    else:
                        print("PLAYER 2: enter valid input ('v' or 'h')")
                ok3 = False
                while not ok3:
                    col_str = input("PLAYER 2: Choose the column number for your fence")
                    if col_str in "12345678":
                        col_int = int(col_str)
                        if col_int < 9 and col_int > 0:
                            col = col_int
                            ok3 = True
                        else:
                            print("PLAYER 2: Please choose an integer bewteen 1 and 8, inclusive")
                    else:
                        print("PLAYER 2: Please choose an integer between 1 and 8, inclusive")
                ok4 = False
                while not ok4:
                    row_str = input("PLAYER 2: Choose the row number for your fence")
                    if row_str in "12345678":
                        row_int = int(row_str)
                        if row_int < 9 and row_int > 0:
                              row = row_int
                              ok4 = True
                        else:
                              print("PLAYER 2: please choose an integer between 1 and 8, inclusive")
                    else:
                        print("PLAYER 2: please choose an integer between 1 and 8, inclusive")
            
                doneplacingfence = placeFence(fence, orient, col, row)
            else:
                print("PLAYER 2: input not valid (type: 'm' or 'f')")


            
        
    

wn = turtle.Screen()
wn.bgcolor("DarkSalmon")

drawer = turtle.Turtle()
drawer.speed(0)


fence1 = turtle.Turtle()
fence2 = turtle.Turtle()
fence1.ht()
fence2.ht()
fence2.color("white")
fence1.pensize(4)
fence2.pensize(4)
fence1.up()
fence2.up()
fence1.setposition(-175,175)
fence2.setposition(-175,175)
startingFencePosX = fence1.xcor()
startingFencePosY = fence1.ycor()                       
sfpx = startingFencePosX
sfpy = startingFencePosY                       

P1 = turtle.Turtle()
P2 = turtle.Turtle()
P1.ht()
P2.ht()
P1.speed(2)
P2.speed(2)
  
drawBoard()
accomodatePlayers()

P1.st()
P2.st()

markersh = ["10","20","30","40","50","60","70","80","90","19","29","39","49","59","69","79","89","99"]
markersv = ["01","02","03","04","05","06","07","08","09","91","92","93","94","95","96","97","98","99"]

winP1 = False
winP2 = False

while not winP1 and not winP2:
    callMove(P1, fence1)
    print(P1.position())
    

    if P1.ycor() == -200:
        winP1 = True
        drawer.color("blue")
        drawer.write("Player 1 Wins!", align = "center", font = ("Times New Roman", 40, "normal"))

    elif P1.position() == P2.position():
        movePiece(P1)
        
        
    else:
        callMove(P2, fence2)
        print(P2.position())
        
        if P2.ycor() == 200:
            winP2 = True
            drawer.color("blue")
            drawer.write("Player 2 Wins!", align = "center", font = ("Times New Roman", 40, "normal"))

        elif P1.position() == P2.position():
            movePiece(P2)

    


    








