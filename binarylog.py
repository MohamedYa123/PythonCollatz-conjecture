import math

result = math.log(1.5) / math.log(2)
print(result)
binary_result = bin(int(result*10**16))
print(str(binary_result).replace('0b',''))

