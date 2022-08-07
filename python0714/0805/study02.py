# 문제 1) 이름이 testfile1.txt인 파일을 생성하고 사용자 키보드로 입력한 데이터를 저장하는 프로그램을 작성하세요.
# 0 : 파일 저장 완료, 나머지 입력은 모두 파일에 저장
# 입력이 완료되고 나면 화면에 입력된 애용을 모두 출력

print("-" * 5, "문제", "-" * 5)

f = open("testfile1.txt", "a", encoding="UTF-8")

while True:
    str = input('저장할 문자를 입력하세요.(0 : 파일 저장) : ')
    if str == "0":
        print("저장완료")
        break
    else:
        f.write(str + "\n")

f.close()