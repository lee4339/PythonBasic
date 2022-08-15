import re

print("-" * 5, "정규 표현식 사용하기", "-" * 5)

str = "[a-z]+"
print("검색하고자 하는 패턴 : {0}".format(str))
p = re.compile(str)

print("-" * 5, "match 사용", "-" * 5)
#처음부터 검색해 매칭되는데까지만 나옴
m = p.match("python")
print(m)

m = p.match("py1thon")
print(m)

m = p.match("3 python")   #못찾음
print(m)

print()
print("-" * 5, "search 사용", "-" * 5)
# 전체에서 검색해 젤먼저 매칭되는 단어를 들고옴
print("검색하고자 하는 패턴 : {0}".format(str))

m = p.search("3 python")
print(m)


print()
print("-" * 5, "findall 사용", "-" * 5)
# 매칭되는 단어를 리스트로 들고옴
print("검색하고자 하는 패턴 : {0}".format(str))

result = p.findall("life is too short")  # 공백은 매칭안되기에 그기를 기점으로 잘라서 리스트에 들어옴
print(result)


print()
print("-" * 5, "finditer 사용", "-" * 5)
# 반복 가능한 객체가 됨( for문을 통해 반복)
print("검색하고자 하는 패턴 : {0}".format(str))

result = p.finditer("life is too short")
print(result)


print()
print("-" * 5, "match의 메서드", "-" * 5)

str = "[a-z]+"
p = re.compile(str)
print("검색할 패턴 : {0}".format(str))

print()
print("-" * 5, "match로 검색 시", "-" * 5)

m = p.match("python")
print("정규 표현식으로 검색한 결과 : {0}".format(m))
print("검색된 문자열 : {0}".format(m.group()))
print("검색된 시작 위치 : {0}".format(m.start()))
print("검색된 끝 위치 : {0}".format(m.end()))
print("검색된 전체 위치 : {0}".format(m.span()))


print()
print("-" * 5, "search로 검색 시", "-" * 5)

m = p.search("3 py 1 thon")
print("정규 표현식으로 검색한 결과 : {0}".format(m))
print("검색된 문자열 : {0}".format(m.group()))
print("검색된 시작 위치 : {0}".format(m.start()))
print("검색된 끝 위치 : {0}".format(m.end()))
print("검색된 전체 위치 : {0}".format(m.span()))










