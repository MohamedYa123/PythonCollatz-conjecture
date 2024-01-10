from decimal import getcontext, Decimal
import numpy as np
maindigits=100
getcontext().prec = maindigits
def log(x,b):
    x=Decimal(x)
    n =Decimal(100000000000000000000)
    b=Decimal(b)
    return (x**(1/n)-1)/(b**(1/n)-1)
log215=log(1.5,2)
print(log215)
lim=10**-8
print(log(Decimal('0.9999999999999999999'),Decimal('2')))

for i in range(2,10**100):
    num= log215*i
    diff= round(num)-num
    if(diff<0):
        diff*=-1
    if(diff<=lim):
        print("\n--------------------------------------------------------------------\n                  num satisfies conditions : ",i," \nnum:",num," \ndiff:",diff,"\nPower:",log(i,10),"\n")
    if(i%1000000==0):
        print("App has Reached ",i,"\npow: ",log(i,10))
