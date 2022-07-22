print("-" * 5, "if문 사용하기", "-" * 5)

money = 15000

print("중국집에 갔습니다.")
print("자장면을 주문합니다.")


#단순 if문 : 기존의 소스코드를 그대로 실행하면서 조건이 True일 경우 추가 옵션으로 더 실행하는 방식을 단순 if문이라고 함
if money >= 11000:
    print("군만두를 추가로 주문합니다.")

print("주문한 음식을 맛있게 먹습니다.")



print("-" * 5, "if ~ else문 사용하기", "-" * 5)
# if ~ else : 조건식의 결과가 True 냐 False냐에 따라서 실행하는 소스코드가 달라지는 방식의 if문

like_menu = "자장면"

print("중국집에 갔습니다.")

if like_menu == "자장면":
    print("자장면을 주문합니다.")
else:
    print("짬뽕을 주문합니다.")

print("주문한 음식을 맛있게 먹습니다.")

# input(출력할 문자열) : 사용자의 키보드 입력을 받는 함수
# input() 함수를 통해서 키보드 입력을 받은 데이터는 모두 문자열
test1 = input()
print(test1)

test2 = input("문자를 입력하세요 : ")
print("입력한 문자는 : {0}".format(test2))

