import sys


def asfoijaf(x):
    print(x)
    

sys.set_int_max_str_digits(1000000000)


def squaring(square):
    square=square*square
    return square


# 3**3**3

def tetration(superbase,supersquare):
    idk=superbase
    for y in range(supersquare-1):
        idk=superbase**idk
    return idk


def pentation(supersuperbase, supersupersquare):
    idkblud=supersuperbase
    for ohnoes in range(supersupersquare-1):
        idkblud=tetration(supersuperbase,idkblud)
    return idkblud

print(pentation(3,2))        

def hexation(verygoodbase, verygoodsquare):
    idktbh=verygoodbase
    for y in range(verygoodsquare-1):
        idktbh=pentation(verygoodbase,idktbh)
    return idktbh

