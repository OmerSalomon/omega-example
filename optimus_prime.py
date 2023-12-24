import math
def isPrime(num: int):
    if num == 2:
        return True
    for i in range(2, int(num / 2)):
        if num % i == 0:
            return False
    return True

def main():
    try:
        num = input()
        isPrime(num)
    except Exception as e:
        print(e)
