import math
def isPrime(num):
    if num == 2:
        return  True
    for i in range(2, int(num/2)):
        if num%i == 0:
            return False
    return True

