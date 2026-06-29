import random
sansfromundertale=1
suffering=random.randint(1,10000)
gambling=0
gamblingtwowin=0
gamblingtwoloss=0

while sansfromundertale==1:
    windowsbluescreenofdeath=True
    computerreallylikesplayingthisgame=random.randint(1,3)
    kjoarwefjoefrowej=random.randint(1,3)

    if kjoarwefjoefrowej==1:
        therizzler="ohio skibidi toilet true sigma mango stinky aura"
    elif kjoarwefjoefrowej==2:
        therizzler="stephen hawkings was on the island"
    elif kjoarwefjoefrowej==3:
        therizzler="you died irl gg l bozo"

    # 1=rock 2=paper 3=scissors
    paperrocksiccsword=input("paper rock or scissors? ")
    x="rock"
    y="paper"
    z="scissors"
    if paperrocksiccsword=="paper" or paperrocksiccsword=="Paper" or paperrocksiccsword=="PAPER":
        if computerreallylikesplayingthisgame==1:
            print("you won, wow. they chose "+x)
            windowsbluescreenofdeath=False
            gamblingtwowin+=1
        elif computerreallylikesplayingthisgame==2:
            print("you tied, wow. they chose "+y)
        elif computerreallylikesplayingthisgame==3:
            print("you suck, wow. they chose "+z)
            gamblingtwoloss+=1
        print("you've won "+str(gamblingtwowin)+" times and lost "+str(gamblingtwoloss)+" times")
    elif paperrocksiccsword=="rock" or paperrocksiccsword=="Rock" or paperrocksiccsword=="therockdwanejohnson":
        if computerreallylikesplayingthisgame==3:
            print("you won, wow. they chose "+z)
            windowsbluescreenofdeath=False
            gamblingtwowin+=1
        elif computerreallylikesplayingthisgame==1:
            print("you tied, wow. they chose "+x)
        elif computerreallylikesplayingthisgame==2:
            print("you suck, wow. they chose "+y)
            gamblingtwoloss+=1
        print("you've won "+str(gamblingtwowin)+" times and lost "+str(gamblingtwoloss)+" times")
    elif paperrocksiccsword=="scissors" or paperrocksiccsword=="Scissors" or paperrocksiccsword=="scossors":
        if computerreallylikesplayingthisgame==2:
            print("you won, wow. they chose "+y)
            windowsbluescreenofdeath=False
            gamblingtwowin+=1
        elif computerreallylikesplayingthisgame==3:
            print("you tied, wow. they chose "+z)
        elif computerreallylikesplayingthisgame==1:
            print("you suck, wow. they chose "+x)
            gamblingtwoloss+=1
        print("you've won "+str(gamblingtwowin)+" times and lost "+str(gamblingtwoloss)+" times")
    else:
        print("我喜欢冰池灵")
    


    if not windowsbluescreenofdeath:
        iwirwiojfwe=input("Do you want to escape? ")
        if iwirwiojfwe=="yes" or iwirwiojfwe=="Yes" or iwirwiojfwe=="YES":
            gambling=gambling+1
            nihao=int(input("Guess a number between 1-10000 "))
            if nihao==suffering:
                sansfromundertale=2
                print("wow")
                print("you took a total of "+str(gambling)+" guesses")
            elif nihao<suffering:
                print("you suck, too low")
            elif nihao>suffering:
                print("you suck, too high")
    
        
    else:
        print(therizzler)

            
    