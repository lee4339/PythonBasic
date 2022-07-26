print("=" * 10, "반복문 사용하기", "=" * 10)

print("-" * 10, "while 문", "-" * 10)

tree_hit = 0 # 초기화 변수, 카운트 변수

while tree_hit < 10:      # 조건식
    tree_hit = tree_hit + 1
    print("나무를 {0}번 찍었습니다".format(tree_hit))

    if(tree_hit == 10):
        print("나무가 넘어갑니다.")

print("-" * 10, "직접 출력", "-" * 10)
print("나무를 1번 찍었습니다")
print("나무를 2번 찍었습니다")
print("나무를 3번 찍었습니다")
print("나무를 4번 찍었습니다")
print("나무를 5번 찍었습니다")
print("나무를 6번 찍었습니다")
print("나무를 7번 찍었습니다")
print("나무를 8번 찍었습니다")
print("나무를 9번 찍었습니다")
print("나무를 10번 찍었습니다")
print("나무가 넘어갑니다.")

print()

count = 0
while count < 10:
    print(count)
    count = count + 1

#조건식이 처음부터 false일 경우는 단 한번도 실행안함

# while 문 사용 시 주의점
# 1. 조건식 및 증감식을 사용 시 무한 반복이 되지 않도록 해야 함
# 1-1 증감식을 생략했을 경우
# 1-2 의도적으로 무한 반복을 사용했을 경우 반드시 탈출 방법을 제시해야함
# 2. 증감식의 위치에 따라 반복문의 결과가 달라짐



print("=" * 10, "break / continue", "=" * 10)

# break : while문 실행 시 break를 만나면 즉시 while문의 실행을 정지하고 while문에서 탈출
# continue : while문 실행 시 continue를 만나면 현재 루프를 종료하고 다음번 루프로 이동

print("-" * 5, "break 사용시", "-" * 5)
count = 0

while count < 10:
    count = count + 1

    if count == 5:
        break;

    print("현재 count의 값: {0}".format(count))



print("-" * 5, "continue 사용시", "-" * 5)
count = 0

while count < 10:
    count = count + 1

    if count == 5:
        continue;

    print("현재 count의 값: {0}".format(count))