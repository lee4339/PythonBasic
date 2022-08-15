# 대본 : https://fangj.github.io/friends/#


import re

# 드라마 프렌즈 시즌1의 1화 대본 파일 열기
f = open("friends101.txt", "r", encoding="UTF-8")
# 파일의 모든 내용 읽어오기
script01 = f.read()
# 파일 닫기
f.close()

# 읽어온 데이터 확인
print(script01[:100])

print()

# Monica의 대사만 가져오기 위해서 정규표현식 패턴 생성
p = re.compile(r"Monica:.+")
# findall()을 사용하여 패턴에 맞는 모든 데이터 가져와서 리스트에 저장
line = p.findall(script01)  #리스트로 모니카 부분만 가져옴

# print(line[:3])

print()

# 지정한 캐릭터의 대사만 저장할 빈 변수 생성
monica = ""
# 리스트에 저장된 데이터를 monica 변수에 대입하기
for item in line:
    monica = monica + item + "\n"  # 줄바꿈 문자 추가

# 지정한 캐릭터 이름의 파일 생성
f = open("monica.txt", "w", encoding="UTF-8")
# 저장된 데이터를 파일에 쓰기
f.write(monica)
f.close()

# 문제 1) Joey의 대사를 추출하여 joey.txt 파일에 모두 저장하는 프로그램을 작성하세요.

p = re.compile(r"Joey:.+")
list_joey = p.findall(script01)

joey = ""

for item in list_joey:
    joey = joey + item + "\n"

f = open("joey.txt", "w", encoding="UTF-8")
# for item in list_joey:
#   f.write(item + "\n")
f.write(joey)
f.close()
