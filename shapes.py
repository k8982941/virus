# s uEW
saswpe=input("big how shape be? ")
saswpe=int(saswpe)

for y in range(saswpe):
    for x in range(saswpe):
        print("* ", end="")
    print()

print()


for y in range(saswpe):
    for x in range(saswpe):
        if y<=0 or y>=saswpe-1 or x<=0 or x>=saswpe-1:
            print("* ", end="")
        else:
            print("  ", end="")

    print()







print()




# ight ianrl    

ghttrangle=input("how long be shape be? ")
ghttrangle=int(ghttrangle)

for a in range(1,ghttrangle+1):
    for b in range(a):
        print("* ", end="")
    print()

print()

for c in range(ghttrangle,0,-1):
    for d in range(c):
        print("* ", end="")
    print()

print()

for rftg in range(ghttrangle):
    for fargwe in range(rftg):
        print("  ", end="")
    for ijorge in range(ghttrangle-rftg):
        print("* ", end="")
    print()





