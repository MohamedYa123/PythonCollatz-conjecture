dd=1
stepsmax=1
def conjcture(n):
    b=n
    bl=True
    stp=0
    while(n>=b ):
       # print(n)
        if(n%3==0):
            n=n/3
            bl=True
        else:
            if(bl):
                dd=n%3
                #bl=False
            n=(4*n-dd)
        stp+=1
    return stp
    #print("Stop")
stepsmax=0
x=0
#conjcture(31)
for i in range(100000,100000000000):
    stp= conjcture(i)
    if(stp>stepsmax):
        stepsmax=stp
    if(i%500000000):
        x+=1
        print(x,"- Max steps:",stepsmax)