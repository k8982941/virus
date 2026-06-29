x=[0,1]
numb=input("how many number ")
for i in range(2,int(numb)):
    fib=x[i-2]+x[i-1]
    x.append(fib)

for y in range(0,len(x)):
    print(x[y])



#0,1,1,2,3,5,8,13,21
