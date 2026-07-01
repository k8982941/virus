ship=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]

emptylsiot=[]
for x in range(6):
    emptylsiot.append([])
    for y in range(4):
        emptylsiot[x].append(" ")


for z in range(len(emptylsiot)):
    for letterafterz in range(len(emptylsiot[z])):
        if len(ship)==0:
            break
        emptylsiot[z][letterafterz]=ship.pop(0)
        
for a in range(3,0,-1):
    for b in range(4):
         emptylsiot[6-a][b]=emptylsiot[a-1][b]


print(emptylsiot)
