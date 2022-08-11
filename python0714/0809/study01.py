# 해당 모듈에 있는 모든 함수, 변수, 클래스를 다 가져옴
# 반드시 모듈명. 함수/변수/클래스명 형태로 사용해야함
import mod1
# 해당 모듈에 있는 함수, 변수, 클래스 중 지정한 것만 가져옴
# 모듈명을 생략할 수 있음
# from mod2 import remainder
# from mod2 import square
# 동일한 모듈에서 여러개의 함수/변수/클래스 한번에 가져오기
from mod2 import remainder, square
import  mod3

print("-" * 5, "모듈 사용하기", "-" * 5)

def multi(a, b):
    return a * b

def div(a, b):
    return a / b

result = multi(10, 20)
print("두 수의 곱셉은 : {0}".format(result))

result = div(10, 3)
print("두 수의 나눗셈은 : {0}".format(result))


result = mod1.add(10, 20)
print("두 수의 덧셈은 : {0}".format(result))

result = mod1.sub(10, 20)
print("두 수의 뺄셈은 : {0}".format(result))

result = remainder(10, 3)
print("두 수의 나눈 후 나머지는 : {0}".format(result))

result = square(10, 3)
print("{0}의 {1} 제곱은 : {2}".format(10, 3, result))


result = mod3.add(10, 20)
print("mod3 모듈을 사용한 두 수의 덧셈은 : {0}".format(result))

result = mod3.sub(10, 20)
print("mod3 모듈을 사용한 두 수의 뺄셈은 : {0}".format(result))