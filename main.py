def main():
    op = 0
    while op != -1:
        print("enter first operand")
        num1 = int(input())
        print("enter second operand")
        num2 = int(input())
        print("choose 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for power")
        print("choose -1 for exit")
        op = int(input())

        if op == 1:
            add(num1, num2)
        elif op == 2:
            sub(num1, num2)
        elif op == 3:
            mult(num1, num2)
        elif op == 4:
            div(num1, num2)
        elif op == 5:
            power(num1, num2)
        else:
            print("Invalid choice. Please choose a valid operation.")

    print("bye bye")

def add(num1, num2):
    print(num1 + num2)

def sub(num1, num2):
    print(num1 * num2)

def mult(num1, num2):
    print(num1 * num2)

def div(num1, num2):
    print(num1 / num2)

def power(num1, num2):
    print(num1 ** num2)

if __name__ == '__main__':
    main()