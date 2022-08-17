import re

print("-" * 5, "정규 표현식과 파일 함수 사용하기", "-" * 5)

# open(파일경로, 파일사용모드, 인코딩)
# 파일경로 : 폴더명 + 파일이름 + 확장자명
# 파일사용모드 : r(읽기), w(쓰기), a(추가)
# 인코딩 : 한글과 같은 비영어 파일 오픈할 경우 encoding = "UTF-8"로 설정
# read(읽을 데이터 수) : 매개변수가 없을 경우는 파일의 모든 데이터를 가져옴, 매개변수가 있을 경우 지정한 크기만큼 가져옴
# readline() : \n을 하나의 라인으로 하여 한줄씩 데이터를 가져옴
# readlines() : \n을 기준으로 모든 데이터를 가져와서 리스트에 저장
# write(입력할 데이터) : 파일에 데이터를 씀
# close() : open()으로 열고 있는 파일을 닫음

# re모듈 : 파이썬에서 정규표현식을 사용하기 위한 모듈
# compile() : 정규표현식의 패턴을 지정하기 위한 함수
# match() : 처음부터 지정한 패턴이 매칭되는 문자열이 있는지 확인
# search() : 전체 데이터 중에서 지정한 패턴이 매칭되는 문자열이 있는지 확인
# findall() : 전체 데이터 중에서 지정한 패턴과 매칭되는 모든 문자열을 리스트에 저장
# finditer() : findall()과 동일하지만 반복 가능한 객체로 생성

# 미드 프렌즈 시즌 1, 2화 대본 열기
f = open('friends102.txt', 'r', encoding="UTF-8")
# 모든 데이터 가져오기
script102 = f.read()
f.close()

# Rachel의 대사에 대한 패턴 생성
p = re.compile(r"Rachel:.+")

line = p.findall(script102)

rachel = ""

for item in line:
    rachel = rachel + item + "\n"

f = open("rachel.txt", "w", encoding="UTF-8")
f.write(rachel)
f.close()


print()
print("-" * 5, "등장인물만 가져오기", "-" * 5)
# 등장인물의 지문 부분을 전부 가져옴
p = re.compile(r"[A-Za-z]+:")
# 등장인물 모두 가져왔지만 중복이 존재함
data_chars = p.findall(script102)
# 중복제거를 위해 set() 사용
set_chars = set(data_chars)
# 중복을 제거한 데이터를 다시 list로 변경
list_chars = list(set_chars)

print(list_chars)

list_chars2 = []
# sub()를 사용하여 기존 문자열을 다른 문자열로 변경
for item in list_chars:
    item = re.sub(":", "", item)
    list_chars2.append(item)

print(list_chars2)

print()
print("-" * 5, "대본 중 지문 부분만 가져오기", "-" * 5)
# 대본 중 지문 부분을 가져오기
# \( : 메타문자 (가 아닌 문자로써의 (를 표현
# \) : 메타문자 )가 아닌 문자로써의 )를 표현
# [A-Za-z] : 괄호 다음에 공백없이 영문자
# .+ : 문자/ 숫자/ 빈칸 등이 1개 이상 반복
# [a-z|\.] : 마지막 문자가 영어 소문자 혹은 마침표
p = re.compile(r"\([A-Za-z].+[a-z|\.]\)")
line2 = p.findall(script102)

print(line2[:5])


print()
print("-" * 5, "특정 단어의 예문만 모아 파일로 저장하기", "-" * 5)
# 특정 단어의 예문만 모아서 파일로 만들기
f = open('friends102.txt', 'r', encoding="UTF-8")
sentences = f.readlines()
f.close()

take = ""

for item in sentences:
    if re.match(r'[A-Z][a-z]+:', item):
        # print(item)
        # take 들어있는 문장만 출력
        if re.search(r"take", item):
            print(item)
            take = take + item + "\n"

f = open('take.txt', 'w', encoding='UTF-8')
f.write(take)
f.close()



