# 문제 1) while문을 이용해서 1 ~ 20까지 출력하는 프로그램을 작성하세요.
print("-" * 5, "문제 1번", "-" * 5)
count = 0
while count < 20:
    count = count + 1
    print(count)

# 문제 2) while문을 이용해서 1 ~ 20까지의 숫자 중 짝수인 것만 출력하는 프로그램을 작성하세요.
print("-" * 5, "문제 2번", "-" * 5)
count = 0
while count < 20:
    count = count + 1

    if count % 2 == 1:
        continue

    print(count)

#while count < 20:
#    count = count + 1
#    if count % 2 == 1:
#        print(count)

# 문제 3) while문을 이용해서 1 ~ 20까지의 숫자 중 3의 배수만 출력하는 프로그램을 작성하세요.
print("-" * 5, "문제 3번", "-" * 5)
count = 0
while count < 20:
    count = count + 1
    if count % 3 == 0:
        print(count)

# 문제 4) while문을 이용해서 1 ~ 10까지의 합을 출력하는 프로그램을 작성하세요.
print("-" * 5, "문제 4번", "-" * 5)
count = 0
sum = 0
while count < 10:
    count = count + 1
    sum = sum + count
    print(sum)
print("전체 합 : {0}".format(sum))

# 문제 5) while문을 이용해서 구구단 중 5단을 출력하는 프로그램을 작성하세요.
# 출력형태 : 5 * 1 = 5 ~ 5 * 9 = 45
print("-" * 5, "문제 5번", "-" * 5)

dan = 5
count = 0
mul = 0

while count < 9:
    count = count + 1
    mul = dan * count
    print("5 * {0} = {1}".format(count, mul))


count = 1
while count < 10:
    print("{0} * {1} = {2}".format(5, count, 5 * count))

    count = count + 1


print("추가")
while True:
    dan = int(input("출력하고자 하는 단수의 숫자를 입력하세요 (2 ~ 9): "))

    if dan == 0:
        print("프로그램을 종료합니다.")
        break
    elif dan < 2:
        dan = 2
        print("2보다 작은 수가 입력되어 기본값인 2로 설정되었습니다.")
    elif dan > 9:
        dan = 9
        print("9보다 큰 수가 입력되어 기본값인 9로 설정되었습니다.")


    count = 1

    while count < 10:
        print("{0} * {1} = {2}".format(dan, count, dan * count))
        count = count + 1

