def sudoku_solver(sudoku):
    if len(sudoku)==9:
        Ok = True
        for k in range(9):
            if len(sudoku[k])!=9:
                Ok = False

        print(Ok)
        if Ok:
            OK = True
            for r in range(9):
                for s in range(9):
                    if sudoku[r][s] not in [0,1,2,3,4,5,6,7,8,9]:
                        OK = False
            print(OK)
            if OK:
                okay = True
                count = 0
                for r in range(9):
                    for s in range(9):
                        if sudoku[r][s] in [1,2,3,4,5,6,7,8,9]:
                            count+=1
                if count<17:
                    okay = False
                print(okay)
                if okay:  
                    return complete_sudoku(sudoku)
                    
def complete_sudoku(sudoku):
    lista0, lista1, lista2, lista3, lista4, lista5, lista6, lista7, lista8 = [sudoku[0][x] for x in range(9)], [sudoku[1][x] for x in range(9)], [sudoku[2][x] for x in range(9)], [sudoku[3][x] for x in range(9)], [sudoku[4][x] for x in range(9)], [sudoku[5][x] for x in range(9)], [sudoku[6][x] for x in range(9)], [sudoku[7][x] for x in range(9)], [sudoku[8][x] for x in range(9)]
    savedinfo = []
    sudokup = [lista0[:], lista1[:], lista2[:], lista3[:], lista4[:], lista5[:], lista6[:], lista7[:], lista8[:]]
    done = False
    impossible = False
    while not done:
        i=0
        j=0
        while sudokup[i][j] != 0:
            if j<=8:
                if j==8:
                    j=0
                    i+=1
                else:
                    j+=1
        restrictions = [sudokup[i][x] for x in range(9) if sudokup[i][x] != 0]+[sudokup[x][j] for x in range(9) if sudokup[x][j] != 0]+[sudokup[3*(int(i/3))+r][3*(int(j/3))+s] for r in range(3) for s in range(3) if sudokup[3*(int(i/3))+r][3*(int(j/3))+s] != 0]
        possibilities = [x for x in range(1,10) if x not in restrictions]
        notinsavedinfo = True
        for w in range(len(savedinfo)):
            if i==savedinfo[w][-2] and j==savedinfo[w][-1]:
                notinsavedinfo = False
        if notinsavedinfo:
            savedinfo.append(possibilities)
            savedinfo[-1].append(i)
            savedinfo[-1].append(j)
        sudokup[i][j]=savedinfo[-1][0]
        if is_sudoku_possible(sudokup):
            fill_sudoku(sudokup)
        else:
            savedinfo[-1]=savedinfo[-1][1:]
            if len(savedinfo[-1])==1:
                savedinfo.pop()
                if len(savedinfo)!=0:
                    savedinfo[-1]=savedinfo[-1][1:]
            if len(savedinfo)!=0:
                done2= False
                while not done2:
                    if len(savedinfo)!=0:
                        if len(savedinfo[-1])==2:
                            savedinfo.pop()
                            if len(savedinfo)!=0:
                                savedinfo[-1]=savedinfo[-1][1:]
                        else:
                            done2=True
                    else:
                        done2=True
            sudokup = [lista0[:], lista1[:], lista2[:], lista3[:], lista4[:], lista5[:], lista6[:], lista7[:], lista8[:]]
            if len(savedinfo)!=0:
                for z in range(len(savedinfo)):
                    sudokup[savedinfo[z][-2]][savedinfo[z][-1]]=savedinfo[z][0]

        done = True
        for t in range(9):
            for w in range(9):
                if sudokup[t][w]==0:
                    done = False

        if len(savedinfo)==0:
            done = True
            impossible = True

    return sudokup if not impossible else None

def complete_sudoku1(sudoku):
    lista0, lista1, lista2, lista3, lista4, lista5, lista6, lista7, lista8 = [sudoku[0][x] for x in range(9)], [sudoku[1][x] for x in range(9)], [sudoku[2][x] for x in range(9)], [sudoku[3][x] for x in range(9)], [sudoku[4][x] for x in range(9)], [sudoku[5][x] for x in range(9)], [sudoku[6][x] for x in range(9)], [sudoku[7][x] for x in range(9)], [sudoku[8][x] for x in range(9)]
    savedinfo = []
    sudokup = [lista0[:], lista1[:], lista2[:], lista3[:], lista4[:], lista5[:], lista6[:], lista7[:], lista8[:]]
    done = False
    impossible = False
    while not done:
        i=0
        j=0
        while sudokup[i][j] != 0:
            if j<=8:
                if j==8:
                    j=0
                    i+=1
                else:
                    j+=1
        restrictions = [sudokup[i][x] for x in range(9) if sudokup[i][x] != 0]+[sudokup[x][j] for x in range(9) if sudokup[x][j] != 0]+[sudokup[3*(int(i/3))+r][3*(int(j/3))+s] for r in range(3) for s in range(3) if sudokup[3*(int(i/3))+r][3*(int(j/3))+s] != 0]
        possibilities = [x for x in range(1,10) if x not in restrictions]
        notinsavedinfo = True
        for w in range(len(savedinfo)):
            if i==savedinfo[w][0] and j==savedinfo[w][1]:
                notinsavedinfo = False
        if notinsavedinfo:
            savedinfo.append(possibilities)
            savedinfo[-1].insert(0,i)
            savedinfo[-1].insert(1,j)
        sudokup[i][j]=savedinfo[-1][-1]
        if is_sudoku_possible(sudokup):
            fill_sudoku(sudokup)
        else:
            savedinfo[-1]=savedinfo[-1][:-1]
            if len(savedinfo[-1])==1:
                savedinfo.pop()
                if len(savedinfo)!=0:
                    savedinfo[-1]=savedinfo[-1][:-1]
            if len(savedinfo)!=0:
                done2= False
                while not done2:
                    if len(savedinfo)!=0:
                        if len(savedinfo[-1])==2:
                            savedinfo.pop()
                            if len(savedinfo)!=0:
                                savedinfo[-1]=savedinfo[-1][:-1]
                        else:
                            done2=True
                    else:
                        done2=True
            sudokup = [lista0[:], lista1[:], lista2[:], lista3[:], lista4[:], lista5[:], lista6[:], lista7[:], lista8[:]]
            if len(savedinfo)!=0:
                for z in range(len(savedinfo)):
                    sudokup[savedinfo[z][0]][savedinfo[z][1]]=savedinfo[z][-1]

        done = True
        for t in range(9):
            for w in range(9):
                if sudokup[t][w]==0:
                    done = False

        if len(savedinfo)==0:
            done = True
            impossible = True

    return sudokup if not impossible else None


def is_sudoku_possible(sudoku):
    llista0, llista1, llista2, llista3, llista4, llista5, llista6, llista7, llista8 = [sudoku[0][x] for x in range(9)], [sudoku[1][x] for x in range(9)], [sudoku[2][x] for x in range(9)], [sudoku[3][x] for x in range(9)], [sudoku[4][x] for x in range(9)], [sudoku[5][x] for x in range(9)], [sudoku[6][x] for x in range(9)], [sudoku[7][x] for x in range(9)], [sudoku[8][x] for x in range(9)]
    sudokuq = [llista0[:], llista1[:], llista2[:], llista3[:], llista4[:], llista5[:], llista6[:], llista7[:], llista8[:]]
    possible = True
    for z in range(81):
        for i in range(9):
            for j in range(9):
                if sudokuq[i][j]==0:
                    restrictions = [sudokuq[i][x] for x in range(9) if sudokuq[i][x] != 0]+[sudokuq[x][j] for x in range(9) if sudokuq[x][j] != 0]+[sudokuq[3*(int(i/3))+r][3*(int(j/3))+s] for r in range(3) for s in range(3) if sudokuq[3*(int(i/3))+r][3*(int(j/3))+s] != 0]
                    possibilities = [x for x in range(1,10) if x not in restrictions]
                    
                    if len(possibilities) == 1:
                        sudokuq[i][j]=possibilities[0]
                    elif len(possibilities) == 0:
                        possible = False
                    
    
    return possible

def fill_sudoku(sudoku):
    sudokup=sudoku[:]
    impossible = False
    for z in range(81):
        for i in range(9):
            for j in range(9):
                if sudokup[i][j]==0:
                    restrictions = [sudokup[i][x] for x in range(9) if sudokup[i][x] != 0]+[sudokup[x][j] for x in range(9) if sudokup[x][j] != 0]+[sudokup[3*(int(i/3))+r][3*(int(j/3))+s] for r in range(3) for s in range(3) if sudokup[3*(int(i/3))+r][3*(int(j/3))+s] != 0]
                    possibilities = [x for x in range(1,10) if x not in restrictions]
                    
                    if len(possibilities) == 1:
                        sudokup[i][j]=possibilities[0]
                    elif len(possibilities) == 0:
                        impossible = True
                    

    return sudokup

game3 = [["0" for x in range(9)] for y in range(9)]
game1 = [[0, 6, 0, 0, 0, 3, 0, 9, 1],
[0,0,0,0, 0, 0, 0, 0, 0],
[0,0,0, 0, 6, 0, 0,0, 0],
[9, 0, 0, 0, 0, 8, 0, 0, 0],
[0, 3, 0,0,0,0,0, 8, 2],
[0,0,0, 9, 0, 0, 0, 0, 4],
[6, 5, 0,0, 1, 0, 0,0,0],
[0,0, 0, 0, 9, 0, 0, 0, 0],
[1, 8, 0, 0, 0, 0, 0, 0, 0]]

olive = [[0,5,0,0,3,0,0,0,9],[0,8,0,0,0,7,4,1,0],[7,0,6,0,0,1,0,0,0],[0,0,7,0,0,5,0,0,0],[0,0,9,7,0,4,8,0,0],[0,0,0,3,0,0,9,0,0],[0,0,0,4,0,0,3,0,8],[0,2,3,6,0,0,0,7,0],[1,0,0,0,7,0,0,9,0]]
olive2 = [[0,0,0,5,3,0,1,0,0],[3,0,0,0,0,8,7,0,0],[1,0,0,0,0,0,4,0,5],[0,6,0,4,0,0,8,0,0],[0,9,0,6,0,1,0,2,0],[0,0,1,0,0,9,0,6,0],[6,0,8,0,0,0,0,0,3],[0,0,2,8,0,0,0,0,1],[0,0,7,0,4,6,0,0,0]]

print(sudoku_solver(olive2))
