print("-" * 5, "elif 문 사용하기", "-" * 5)

score = input("당신의 점수를 입력해주세요 : ")
score = int(score)

if score >= 90:
    print("당신의 점수는 {0}점이고, 등급은 A입니다.".format(score))
elif score >= 80:
    print("당신의 점수는 {0}점이고, 등급은 B입니다.".format(score))
elif score >= 70:
    print("당신의 점수는 {0}점이고, 등급은 C입니다.".format(score))
elif score >= 60:
    print("당신의 점수는 {0}점이고, 등급은 D입니다.".format(score))
else:
    print("당신의 점수는 {0}점이고, 등급은 F입니다.".format(score))




print("\n\n", "-" * 5, "elif 문에 else 생략하기", "-" * 5)
# elif 문의 else 문은 반드시 입력해야하는 것은 아니며 생략이 가능
# elif 문을 통해서 발생할 수 있는 모든 조건을 입력하면 else문을 생략해도 상관없음
# 지정한 조건을 제외하고는 연산을 진행하지 않고 그냥 넘어갈 경우 else문을 생략할 수 있음
if score >= 90:
    print("당신의 점수는 {0}점이고, 등급은 A입니다.".format(score))
elif score >= 80:
    print("당신의 점수는 {0}점이고, 등급은 B입니다.".format(score))
elif score >= 70:
    print("당신의 점수는 {0}점이고, 등급은 C입니다.".format(score))
elif score >= 60:
    print("당신의 점수는 {0}점이고, 등급은 D입니다.".format(score))
elif score < 60:
    print("당신의 점수는 {0}점이고, 등급은 F입니다.".format(score))


print("\n\n")
#문제 1) input을 통해서 사용자 입력을 숫자로 1 ~ 5까지 입력받고, 입력된 숫자에 해당하는 메뉴를        출력하는 프로그램을 작성하세요.
# 1 : 자장면, 2 : 짬뽕, 3 : 우동, 4 : 볶음밥, 5 : 잡채밥
# elif 문을 사용하여 프로그램 작성
# 입력된 숫자가 1 ~ 5까지의 숫자가 아닐 경우 "잘못된 입력입니다." 출력

print("중국집에서 음식을 주문합니다.")
menu = int(input("메뉴 1번부터 5번까지 중 선택해주세요.(1:자장면, 2:짬뽕, 3:우동, 4:볶음밥, 5:잡채밥) : "))

if menu == 1:
    print("선택하신 메뉴는 자장면입니다.")
elif menu == 2:
    print("선택하신 메뉴는 짬뽕입니다.")
elif menu == 3:
    print("선택하신 메뉴는 우동입니다.")
elif menu == 4:
    print("선택하신 메뉴는 볶음밥입니다.")
elif menu == 5:
    print("선택하신 메뉴는 잡채밥입니다.")
else:
    print("선택하신 메뉴는 존재하지 않습니다.")