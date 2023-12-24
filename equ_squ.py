import math

def equ_squ(a, b, c):
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (+b + math.sqrt(b * b - 4 * a * c)) / (2 * a)

def main():
    try:
        a = input()
        b = input()
        c = input()
        equ_squ(a, b, c)
    except Exception as e:
        print(e)

