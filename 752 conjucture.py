def conjcture(i,b):
    steps=0
    while(i>=b and i>1):
        if(i%2==0):
            i=i/2
        else:
            i=(i*3+1)/2
        steps+=1
    return steps
def DoConjecture(i):
    return conjcture(i,i)
stepsmax=0
print(DoConjecture(9780657630))
for i in range(977639,10**10,2):
    stp= DoConjecture(i)
    if stp>stepsmax:
         stepsmax=stp
    if i%100001==0:
            print("Reached ",(i+0.0)/10**10,"*10^(10) Numbers")
            print("Max steps found : ",stepsmax)

#input('')