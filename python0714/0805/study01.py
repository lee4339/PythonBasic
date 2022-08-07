print("=" * 10, "파일 사용하기", "=" * 10)

print("-" * 5, "readline() 사용", "-" * 5)
# readline() : 한번 실행 시 파일의 내용을 한줄씩 읽어옴
# 더이상 읽을 내용이 없으면 None을 출력
# 반복문을 사용하여 None이 나올때가지 계속 실행해야 함
f = open("file1.txt", "r", encoding="UTF-8")

while True:
    tmp = f.readline()

    if tmp:
        print(tmp[:-1])
    else:
        break

f.close()


print("-" * 5, "readlines() 사용", "-" * 5)
# readlines() : 한번 실행 시 파일의 모든 내용을 읽어서 리스트로 출력
# 반복문을 사용하여 리스트의 내용을 출력하는 형태로 사용
f = open("file1.txt", "r", encoding="UTF-8")

tmp_list = f.readlines()
#print(tmp_list)
for item in tmp_list:
    item = item[:-1]
    print(item)
f.close()



print("-" * 5, "read() 사용", "-" * 5)
# read() : 한번 실행 시 파일의 모든 내용을 읽어서 문자열로 출력

f = open("file1.txt", "r", encoding="UTF-8")

str_tmp = f.read()
print(str_tmp)

f.close()


print("-" * 5, "문제1", "-" * 5)
f = open("file1.txt", "r", encoding="UTF-8")

list1 = f.readlines()

for i in list1:
    if i[-1] == "\n":
        i = i[:-1]

    print(i)

f.close()


print("-" * 5, "문제2", "-" * 5)
f = open("file1.txt", "r", encoding="UTF-8")


while True:
    list2 = f.readline()

    if not list2:
        break
    if list2[-1] == "\n":
        list2 = list2[0:-1]
    print(list2)



print("\n\n", "-" * 5, "write()/writelines()", "-" * 5)

# 파일 쓰기 함수
# write("문자열") : 입력받은 문자열을 파일에 저장
# 한번 실행 시 하나의 라인씩 저장함
str_list = ["12345", "abcde", "!@#$%", "가나다라마"]

f = open("file2.txt", "w", encoding="UTF-8")

for item in str_list:
    f.write(item +"\n")
# f.write("파일에 내용을 씁니다.\n")
# f.write("write() 함수는 한번 실행 시 한줄씩 입력합니다.")

f.close()

print("파일 저장 완료\n")

# writelines(리스트) : 리스트의 내용을 한번에 파일에 저장
# 리스트에 있는 내용이 하나의 라인에 전부 다 저장됨
# 리스트에 있는 내용이 각각의 라인에 저장될려면 "\n".join 명령을 사용해야한다.

str_list = ["12345", "abcde", "!@#$%", "가나다라마"]

f = open("file3.txt", "w", encoding="UTF-8")

# f.writelines(str_list)
f.writelines("\n".join(str_list))

f.close()

print("writelines() 사용완료")




print("\n\n", "-" * 5, "seek()/tell()", "-" * 5)
# seek(위치) : 파일에서 지정한 위치로 커서를 이동, 파일의 처음 위치는 0
# tell() : 파일에 현재 커서의 위치를 출력
# read(갯수) : read() 함수는 매개변수로 입력하지 않을 경우 모든 데이터를 다 가져옴, 하지만 매개변수로 숫자를 지정하면 현재 커서의 위치에서부터 지정한 갯수의 데이터를 가져옴

f = open("file3.txt", "r", encoding="UTF-8")

print("현재 위치 : {0}".format(f.tell()))
tmp = f.read(4)
print(tmp)
print("현재 위치 : {0}".format(f.tell()))
f.seek(11)
print("현재 위치 : {0}".format(f.tell()))
tmp = f.read(4)
print(tmp)
print("현재 위치 : {0}".format(f.tell()))
f.seek(0)
print("현재 위치 : {0}".format(f.tell()))

f.close()




print("\n\n", "-" * 5, "a모드 사용하기", "-" * 5)

f = open("file4.txt", "a", encoding="UTF-8")

for i in range(1, 6):
    str = "{0}번 데이터를 추가합니다.\n".format(i)
    f.write(str)

f.close()



print("\n\n", "-" * 5, "x모드 사용하기", "-" * 5)

f = open("file5.txt", "x", encoding="UTF-8")

for i in range(1, 6):
    str = "{0}번 데이터를 추가합니다.\n".format(i)
    f.write(str)

f.close()
