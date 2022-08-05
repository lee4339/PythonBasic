print("-" * 10, "전역 변수/지역 변수/global", "-" * 10)

# 전역 변수 : 프로그램 전체에서 사용할 수 있는 변수, 프로그램 종료 시 까지 메모리 상에 존재함
# 지역 변수 : 특정 함수 안에서 선언되고, 사용되고, 삭제되는 변수, 해당 함수 호출 수 메모리에 등록되고,                    해당 함수 호출 완료 시 메모리에서 삭제 됨
# global : 함수 안에서 전역 변수를 사용 시 해당 변수가 전역 변수임을 나타내는 명령어, 전역 변수를 읽어올 경우에는 global없어도 됨

g_value = 100

print("전역변수 g_value의 값 : {0}".format(g_value))

def func1():
    print("함수 1에서 전역변수 g_value 출력 : {0}".format(g_value))

def func2():
    l_value = 10
    print("함수 2에서 전역변수 l_value 출력 : {0}".format(l_value))

def func3():
    # 지역변수 g-value를 선언하고 데이터 1000을 저장
    # 전역변수와 지역변수의 이름이 동일할 경우 지역변수가 우선순위가 높음

    g_value = 1000
    print("함수 3에서 전역변수 g_value 출력 : {0}".format(g_value))

def func4():
    # global 명령어를 사용하면 지정된 변수가 전역 변수임을 알려줌
    global g_value
    g_value = 1000
    print("함수 4에서 전역변수 g_value 출력 : {0}".format(g_value))

# 실행구간
func1()
func2()
# 함수 안의 지역변수는 해당 함수 밖에서 접근이 불가능함.
#print("함수 2 밖에서 함수 2의 지역변수 l_value 출력 : {0}".format(l_value))
func3()
print("전역 변수 g_value 출력 : {0}".format(g_value))

func4()
print("전역 변수 g_value 출력 : {0}".format(g_value))



print("\n\n","-" * 10, "lambda 사용하기", "-" * 10)

def sum1(a, b):
    return a + b

print(sum1(10, 20))


sum = lambda a, b: a + b
sub = lambda a, b: a - b
multi = lambda a, b: a * b
div = lambda a, b: a / b

print(sum(10, 20))
print(sub(10, 20))
print(multi(10, 20))
print(div(10, 20))

