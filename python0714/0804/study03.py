print("-" * 10, "파일 사용하기", "-" * 10)

# OS에서 문자를 표시할 때 사용하는 문자 코드셋이라는 것이 존재함
# 현재 window에서 한글을 표기하는 문자셋이 cp949(iso-8859-1)를 사용함
# 한글 표현 시 오류가 발생하면 open() 함수의 3번째 매개변수에 encoding = "UTF-8" 을 입력

f = open("files.txt", "r", encoding="UTF-8")
#f = open("files2.txt", "r")

while True:
    line = f.readline()

    # if not line:        # 더이상 읽을 내용이 없으면 None
    #     break
    #
    # print(line)

    if line:
        print(line)
    else:
        break

f.close()
