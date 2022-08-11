print("-" * 5, "예외처리 finally사용", "-" * 5)

num1 = int(input("첫번째 숫자를 입력해주세요 : "))
num2 = int(input("두번째 숫자를 입력해주세요 : "))

list_a =[10, 20, 30, 40, 50]
idx = int(input("출력할 index 번호를 입력하세요 : "))

dic_car = {"name": "트위지", "type": "쿠페", "size":"초소형"}

try:
    result = num1 // num2
    print("두 수를 나눈 몫은 : {0}".format(result))
    print("list_a[{0}] : {1}".format(idx, list_a[idx]))
    print("dic_car['name'] : {0}".format(dic_car["color"]))
except ZeroDivisionError as e:
    print(e)
    print("숫자를 0으로 나눌 수 없습니다.")
except IndexError as e:
    print(e)
    print("리스트의 최대 크기를 넘어서는 값을 입력했습니다.")
except KeyError:
    # pass : if, while, for와 같은 코드블럭을 빈 코드블럭으로 만들고 싶을 경우 사용하는 키워드
    # 소스코드가 비어있다라는 의미로 사용함.
    pass
except:
    print("프로그램 실행 중 오류가 발생했습니다.")
finally:
    print("프로그램을 종료합니다.")


menu = "자장면"

# if menu == "짬뽕":
#     print("짬뽕")
# else :
#     pass