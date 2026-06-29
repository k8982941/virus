calculatorlifesupport=1
while calculatorlifesupport==1:
    x=input("Insert your first number or use previous answer by typing 'ans' ")
    y=input("Insert your second number or use previous answer by typing 'ans'                why ")

    z=input("Do you want to +, -, *, /, or ^ these two numbers? ")

    if x=="ans":
        x=skibidi
    else:
        x=float(x)

    if y=="ans":
        y=skibidi
    else:
        y=float(y)

    if z=="+":
        skibidi=x+y
        print(skibidi)
    elif z=="-":
        skibidi=x-y
        print(skibidi)
    elif z=="*":
        skibidi=x*y
        print(skibidi)
    elif z=="/":
        skibidi=x/y
        print(skibidi)
    elif z=="^":
        skibidi=x**y
        print(skibidi)

    
    calculatorlifesupport=float(input("Type 1 to continue calculations, type 2 to end calculations "))

