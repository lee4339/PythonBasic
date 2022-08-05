print("=" * 10, "함수의 형태 4가지", "=" * 10)

# 1. 매개변수 X, 반환값 X
# 함수 실행 시 필요한 데이터(변수)를 함수 내부에서 선언하고 사용하고 삭제됨
# 실행 결과를 함수에서 출력해야 함
# 함수 실행 결과가 동일함
def sum1() :
    a = 10
    b = 20
    result = a + b
    print("두 수의 덧셈 : {0}".format(result))

sum1()
sum1()

# 2. 매개변수 O, 반환값 X
# 함수 실행 시 필요한 데이터(변수)를 외부에서 제공함
# 함수 실행 결과가 달라짐
# 실행 결과를 함수에서 출력해야 함
def sum2(a, b):
    result = a + b
    print("두 수의 덧셈 : {0}".format(result))

sum2(10, 20)
sum2(100, 200)

# 3. 매개변수 X, 반환값 O
# 함수 실행 시 필요한 데이터(변수)를 함수 내부에서 선언하고 사용하고 삭제됨
# 함수 실행 결과가 동일함
# 실행 결과를 함수 외부에서 출력할 수 있음

def sum3():
    a = 10
    b = 20
    result = a + b
    return result

a = sum3()
print(a)
print(sum3())

sum2(10, a)
sum2(sum3(), 100)

# 4. 매개변수 O, 반환값 O
# 함수 실행 시 필요한 데이터(변수)를 외부에서 제공함
# 함수 실행 결과가 달라짐
# 실행 결과를 함수 외부에서 출력할 수 있음

def sum4(a, b):
    result = a + b
    return result

b = sum4(10, 20)
print(b)
print(sum4(10, 20))

sum2(b, 100)
sum2(sum4(10, 20), b)


print("\n\n")
# 문제1) 함수 형태 1번을 사용하여 사칙 연산을 하는 함수를 작성하고 사용하세요.
# 함수 이름 : sum1, sub1, multi1, div1

print("-" * 5, "문제1번", "-" * 5)

sum1()

def sub1() :
    a = 10
    b = 20
    result = a - b
    print("두 수의 뺄셈 : {0}".format(result))
sub1()

def multi1() :
    a = 10
    b = 20
    result = a * b
    print("두 수의 곱셈 : {0}".format(result))
multi1()

def div1() :
    a = 10
    b = 20
    result = a / b
    print("두 수의 나눗셈 : {0}".format(result))
div1()

# 문제2) 함수 형태 2번을 사용하여 사칙 연산을 하는 함수를 작성하고 사용하세요.
# 함수 이름 : sum2, sub2, multi2, div2

print("-" * 5, "문제2번", "-" * 5)

sum2(20, 10)

def sub2(a, b):
    result = a - b
    print("두 수의 뺄셈 : {0}".format(result))
sub2(20, 10)

def multi2(a, b):
    result = a * b
    print("두 수의 곱셈 : {0}".format(result))
multi2(20, 10)

def div2(a, b):
    result = a / b
    print("두 수의 나눗셈 : {0}".format(result))
div2(20, 10)

# 문제2) 함수 형태 3번을 사용하여 사칙 연산을 하는 함수를 작성하고 사용하세요.
# 함수 이름 : sum3, sub3, multi3, div3

print("-" * 5, "문제3번", "-" * 5)

print("두 수의 덧셈 : {0}".format(sum3()))

def sub3():
    a = 10
    b = 20
    result = a - b
    return result
print("두 수의 뺄셈 : {0}".format(sub3()))

def multi3():
    a = 10
    b = 20
    result = a * b
    return result
print("두 수의 곱셈 : {0}".format(multi3()))

def div3():
    a = 10
    b = 20
    result = a / b
    return result
print("두 수의 나눗셈 : {0}".format(div3()))

# 문제3) 함수 형태 4번을 사용하여 사칙 연산을 하는 함수를 작성하고 사용하세요.
# 함수 이름 : sum4, sub4, multi4, div4

print("-" * 5, "문제4번", "-" * 5)

print("두 수의 덧셈 : {0}".format(sum4(20, 10)))

def sub4(a, b):
    result = a - b
    return result
print("두 수의 뺄셈 : {0}".format(sub4(20, 10)))

def multi4(a, b):
    result = a * b
    return result
print("두 수의 곱셈 : {0}".format(multi4(20, 10)))

def div4(a, b):
    result = a / b
    return result
print("두 수의 나눗셈 : {0}".format(div4(20, 10)))


#########################################################################

print("\n\n","-" * 10, "함수 호출 시 매개변수 지정하기", "-" * 10)

def add(a, b):
    result = a + b
    return result

print(add(10, 20))

print(add(a = 10, b = 20))
print(add(b = 10, a = 20))


print("\n\n","-" * 10, "매객변수 초기값 설정", "-" * 10)

# 초기값이 설정된 매개변수는 반드시 가장 마지막에 입력되어야 함
# 초기값이 설정된 매개변수가 중간 혹은 가장 앞에 있을 경우 해당 매개변수를 생락하면 어떠한 매개변수를 생략한 것인지 확인할 수 없기때문에 초기값이 설정된 매개변수를 가장 마지막에 입력함
def say_myself(name, old, man = True):
    print("나의 이름은 {0}입니다.".format(name))
    print("나이는 {0}살 입니다.".format(old))

    if man:
        print("남자 입니다.")
    else:
        print("여자 입니다.")

say_myself("홍길동", 25, True)
say_myself("이순신", 25)
