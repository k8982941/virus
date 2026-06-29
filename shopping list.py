import random

x=[]

while True:
    agreetwoall=input("do you want to continue shop, type yes to confirm, type no to avoid legally binding contract ")

    if agreetwoall=="yes":
        bluecrystals=input("welcome to costco, ADD or REMOVE your list to our ai generated food ADD item food STEAL your ip address prompt ")
        if bluecrystals=="add" or bluecrystals=="ADD":
            adding=input("whatdoyouwanttoadd")
            x.append(adding)
        if bluecrystals=="remove" or bluecrystals=="REMOVE":
            removing=input("whatdoyouwanttoremove")
            if removing in x:
                x.remove(removing)
                print("removed")
            else:
                print("thatsnotinthelist")
        print("your food item ai generated list: "+str(x)+" which will cost "+ str(len(x)*100)+ " dollars")
        if bluecrystals=="steal" or bluecrystals=="STEAL":
            maozedongthought=random.randint(1,3)
            if maozedongthought==1:
                print("you escaped with all of the items for free")
                break
            else:
                print("you were caught and got jailed. spend 2000 years in jail")
                break

        
    else:
        print('bye')
        break
