
print("탕수육 전문점에 탕숙육을 배달시켰습니다.")

choice = input("당신이 탕수육을 먹는 방법은 ? ")

if choice == "부먹":
    print("나는 부먹파 입니다.")
else:
    print("나는 찍먹파 입니다.")

print("\n\n\n")

#중첩 if문 사용하기
membership = "vip"
year = 2

if membership == "vip":
    if year > 2:
        print("이벤트에 참여가 가능합니다.")
        print("등급 : {0}".format(membership))
        print("년차 : {0}".format(year))
        print("좌석 : {0}".format("1 번 라인"))
    else:
        print("이벤트에 참여가 가능합니다.")
        print("등급 : {0}".format(membership))
        print("년차 : {0}".format(year))
        print("좌석 : {0}".format("3 번 라인"))
else:
    print("이벤트에 참여가 불가능합니다.")

print()

# int(문자열 타입인 숫자) : 문자열 타입으로 만들어진 숫자를 정수로 변환
# float("숫자") : 문자열 타입으로 만들어진 숫자를 실수형으로 변환
year = input("당신의 멤버쉽 연차는 : ")
year = int(year)
if year > 4:
    print("이벤트 참여가 가능합니다.")
    if membership == "vip":
        print("등급 : {0}".format(membership))
        print("좌석 : {0}".format(membership + "전용"))