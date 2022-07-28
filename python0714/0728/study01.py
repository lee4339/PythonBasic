print("-" * 5, "for문 사용하기", "-" * 5)

test_list = ["one", "two", "three"]
for i in test_list:
    print(i)


print("-" * 5, "while문 사용하여 출력", "-" * 5)
count = 0

while count < len(test_list):
    print(test_list[count])
    count = count + 1


print("-" * 5, "1 ~ 10 출력", "-" * 5)

count = 1

while count < 11:
    print(count)
    count = count + 1

print()

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)

print()

list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list_num:
    print(i)

print()

# range() : 0 ~ 지정한 숫자까지의 리스트를 생성해주는 함수
# range(시작숫자, 끝숫자) : 마지막 숫자 -1인 형태의 리스트 생성

for i in range(1, 11):
    print("i : {0}".format(i))

print()

for i in range(5, 15):
    print("i : {0}".format(i))

list_num1 = range(10)
print(list_num1)

list_num2 = list(list_num1)
print(list_num2)


print("\n", "-" * 5, "for문을 사용한 구구단", "-" * 5)

dan = int(input("출력하고자 하는 구구단의 단수를 입력해주세요: "))

for i in range(1, 10):
    print("{0} * {1} = {2}".format(dan, i, dan * i))


# 문제 1) for문을 사용하여 2 ~ 9 단까지의 구구단을 모두 출력하는 프로그램을 작성하세요
# 2 중 for문으로 구구단 생성
print("-" * 5, "문제 1", "-" * 5)
for i in range(2, 10):
    print("-" * 3, "{0}단".format(i), "-" * 3)
    for j in range(1, 10):
        print("{0} * {1} = {2}".format(i, j, i * j))



print("")

# print() : print 함수는 이스케이프 문자 \n을 포함하고 있음
# print() 사용 시 줄바꿈을 하지 않을 경우 2번째 매개변수에 end=""를 사용하여 마지막에 들어갈 문자를 변경할 수 있음

print("기본 출력 방식 (줄바꿈 문자 포함)")
print("end='' 옵션 사용 시 1", end="\t") # tap키 사용
print("end='' 옵션 사용 시 2", end="\t")
print("end='' 옵션 사용 시 3", end="\t")
print()
print("end='' 옵션 사용 시 4", end="@@")
print("end='' 옵션 사용 시 5", end="&&")


print("\n", "-" * 5, "리스트 내포 사용하기", "-" * 5)

a = [1, 2, 3, 4]
print("원본 리스트 a : {0}".format(a))
result = []

for num in a:
    result.append(num * 3)
print("결과 리스트 result : {0}".format(result))

print("\n-리스트 내포 방식사용-")
a = [1, 2, 3, 4]
print("원본 리스트 a : {0}".format(a))
result = [num * 3 for num in a]
print("리스트 내포 결과 result : {0}".format(result))

print("\n-리스트 내포 예제2-")
a = [1, 2, 3, 4]
print("원본 리스트 a : {0}".format(a))
result = [num * 3 for num in a if num % 2 == 0]
print("리스트 내포 결과 result : {0}".format(result))

'''
for num in a:
    if num % 2 == 0:
        result.append(num * 3)
print("리스트 내포 결과 result : {0}".format(result))
'''


