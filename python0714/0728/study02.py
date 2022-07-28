print("=" * 10, "함수", "=" * 10)

def add(a, b):
    return a + b

result = add(10, 20)
print(result)


print("\n\n")
'''
# 반복문을 사용하여 중복되는 소스코드를 수정
count = 0

while count < 3:
    score = int(input("당신의 점수를 입력하세요 : "))
    level = "F"

    if score >= 90:
        level = "A"
    elif score >= 80:
        level = "B"
    elif score >= 70:
        level = "C"
    elif score >= 60:
        level = "D"
    #else:
    #    level = "F"
    print("당신의 점수는 {0}점이고, 등급은 {1}입니다.".format(score, level))

    count = count + 1
'''


# 함수를 사용하여 중복되는 소스코드를 수정
def cal_score():
    score = int(input("당신의 점수를 입력하세요 : "))
    level = "F"

    if score >= 90:
        level = "A"
    elif score >= 80:
        level = "B"
    elif score >= 70:
        level = "C"
    elif score >= 60:
        level = "D"

    print("당신의 점수는 {0}점이고, 등급은 {1}입니다.".format(score, level))


cal_score()

count = 0

while count < 3:
    cal_score()
    count = count + 1


