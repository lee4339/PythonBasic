print("-" * 5, "계산", "-" * 5)

def sum():
    a = 10
    b = 20
    c = a + b
    print("두 수의 덧셈은 : {0}".format(c))

def sub():
    a = 10
    b = 20
    c = a - b
    print("두 수의 뺄셈은 : {0}".format(c))

def multi(a, b):
    c = a * b
    print("두 수의 곱셈은 : {0}".format(c))

def div():
    a = 10
    b = 3
    print("두 수의 나눗셈은 : {0}".format(a/b))

sum()
sub()
multi(10, 20)
div()

print()
#문제 2) 숫자를 입력받아서 입력받은 숫자의 구구단 단수를 출력하는 프로그램을 함수를 사용하여 작성하세요.

def gogodan():
    dan = int(input("구구단의 단수를 입력해주세요: "))
    for i in range(1, 10):
        print("{0} * {1} = {2}".format(dan, i, dan * i))

gogodan()