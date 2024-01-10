from decimal import getcontext, Decimal
maindigits=1000
digits=5
getcontext().prec = maindigits
def ln(x):
    x=Decimal(x)
    n =Decimal(100000)
    return n * ((x ** (1/n)) - Decimal(1))
def log(x,b):
    x=Decimal(x)
    n =Decimal(10000000000000000)
    return (x**(1/n)-1)/(b**(1/n)-1)
# Calculate the logarithm of 10 with 500 digits of precision
log_10_with_500_digits = log(1.5,2)
getcontext().prec = digits
j=Decimal(Decimal(1)/(log_10_with_500_digits))
k=Decimal(j*Decimal(10**(digits-1))*Decimal(6))
getcontext().prec = maindigits
getcontext().prec=100
#
d=51.415
d=60
v1=Decimal(3**3*(Decimal(2)**Decimal(d))-1)
v2=Decimal(2**3*(Decimal(2)**Decimal(d))-1)
v=(v1/v2)*Decimal(2**3/3**3)
print("decimal : ",v)
#print(log(v,2))
# Print the result
#print(f"The logarithm of 10 with 500 digits of precision is: {log_10_with_500_digits}")
