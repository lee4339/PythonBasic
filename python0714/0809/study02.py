print("-" * 5, "예외처리", "-" * 5)

test_list = []

# while True:
#     input_num = int(input("숫자를 입력하세요 : (종료 : 0)"))
# 
#     if input_num == 0:
#         break
# 
#     test_list.append(input_num)
# 
# count = int(input("반복 숫자를 입력하세요 : "))
# total = 0


# 오류가 발생할 수 있는 가능성은 2가지인데 예외처리는 한가지 방식으로 통일되어 있음
# 어떤 오류가 발생하여 예외처리를 했는지 알 수 없음
# 발생한 예외에 상관없이 동일한 방식으로 처리
try:
    while count > 0:
        total = total + test_list[count - 1]
        count = count - 1
    print("저장된 총합은 : {0}".format(total))

    num1 = int(input("첫번쨰 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    result = num1 / num2
    print(result)
except:
    print("잘못된 입력으로 오류가 발생했습니다.")

print("프로그램을 종료합니다.")

print()



