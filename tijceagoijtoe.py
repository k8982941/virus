tictacs=[["-","-","-"],
         ["-","-","-"],
         ["-","-","-"]]

def illegalyprintUSdollars(board):
    for y in range(0,3):
        print(" ",end="")
        for x in range(0,3):
            print(board[y][x], end="")
            if x<2:
                print(" | ", end="")
        print()
        if y<2:
            print("-----------")


player="X"

def hirohito(tictacs, rplayed):
    while True:
        inputvariableMKI=int(input("你“y轴”范在哪了? "))-1
        inputvariableMKII=int(input("你“x轴”范在哪了? "))-1
        try:
            if tictacs[inputvariableMKI][inputvariableMKII]=="-":
                tictacs[inputvariableMKI][inputvariableMKII]=rplayed
                return tictacs
            else:
                print("你是猪八戒")
        except IndexError, ValueError, SystemError:
            print("你是猪八戒")


nuclearsilocountdown=0        
    
while True:
    illegalyprintUSdollars(tictacs)
    tictacs=hirohito(tictacs, player)
    if tictacs[0][0]==player and tictacs[0][1]==player and tictacs[0][2]==player:
        illegalyprintUSdollars(tictacs)
        print(player+ " 杀了他的对手!")
        break
    if tictacs[1][0]==player and tictacs[1][1]==player and tictacs[1][2]==player:
        illegalyprintUSdollars(tictacs)
        print(player+ " 杀了他的对手!")
        break
    if tictacs[2][0]==player and tictacs[2][1]==player and tictacs[2][2]==player:
        illegalyprintUSdollars(tictacs)
        print(player+ " 杀了他的对手!")
        break
    if tictacs[0][0]==player and tictacs[1][0]==player and tictacs[2][0]==player:
        illegalyprintUSdollars(tictacs)
        print(player+ " 杀了他的对手!")
        break
    if tictacs[0][1]==player and tictacs[1][1]==player and tictacs[2][1]==player:
        illegalyprintUSdollars(tictacs)
        print(player+ " 杀了他的对手!")
        break
    if tictacs[0][2]==player and tictacs[1][2]==player and tictacs[2][2]==player:
        illegalyprintUSdollars(tictacs)
        print(player+ " 杀了他的对手!")
        break
    if tictacs[0][0]==player and tictacs[1][1]==player and tictacs[2][2]==player:
        illegalyprintUSdollars(tictacs)
        print(player+ " 杀了他的对手!")
        break
    if tictacs[0][2]==player and tictacs[1][1]==player and tictacs[2][0]==player:
        illegalyprintUSdollars(tictacs)
        print(player+ " 杀了他的对手!")
        break
    nuclearsilocountdown+=1
    if nuclearsilocountdown==9:
        illegalyprintUSdollars(tictacs)
        print("平局")
        break
    if player=="X":
        player="O"
    elif player=="O":
        player="X"




    
    
    
    
    

    