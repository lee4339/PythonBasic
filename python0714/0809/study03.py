list_a = [10, 20, 30]

try:
    idx = int(input("출력할 index 번호를 입력하세요 : "))
    print("list_a[{0}] : {1}".format(idx, list_a[idx]))

    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))

    result = num1 / num2
    print(("두 수를 나눈 몫은 : {0}".format(result)))
# 지정한 오류에 대해서만 예외처리 하기
# 여러개의 오류에 대해서 다른 방식으로 예외처리가 가능함
except IndexError:
    print("리스트의 최대 크기를 넘은 값을 입력했습니다.")
except ZeroDivisionError:
    print("0으로는 나눌 수 없습니다.")


print()
print()


list_b = [10, 20, 30, 40, 50]

try:
    idx = int(input("출력할 index 번호를 입력하세요 : "))
    print("list_a[{0}] : {1}".format(idx, list_b[idx]))

    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))

    result = num1 // num2
    print(("두 수를 나눈 몫은 : {0}".format(result)))
# 에러 발생 시 실제 에러 정보를 사용자에게 출력할 수 있음
except IndexError as e:
    print("리스트의 최대 크기를 넘은 값을 입력했습니다.")
    print(e)
except ZeroDivisionError as e:
    print("0으로는 나눌 수 없습니다.")
    print(e)