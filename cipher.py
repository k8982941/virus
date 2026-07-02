def ceasersalad(input,shift):
    shift=int(shift)
    ceasersaldciphe=""
    for unicode in input:
        num=ord(unicode)+shift
        newvariableohioskibidirizzler=chr(num)
        ceasersaldciphe+=newvariableohioskibidirizzler
    return ceasersaldciphe

enemin=ceasersalad("I love skibidi toilet", 7)
print(enemin)

nimene=ceasersalad(enemin,-7)
print(nimene)