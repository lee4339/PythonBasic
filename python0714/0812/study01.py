import re

print("-" * 5,"컴파일 옵션 사용하기", "-" * 5)


print("-" * 5,"DOTALL 옵션", "-" * 5)
# DOTALL : 줄바꿈 문자를 포함하여 모든 임의의 문자와 매칭
# p = re.compile("a.b")  # DOTALL이 없으면 \n 인식못함
# m = p.match("a\nb")

p = re.compile("a.b", re.DOTALL)
m = p.match("a\nb")
print(m)

print()


print("-" * 5,"IGNORECASE 옵션", "-" * 5)
# p = re.compile("[a-zA-Z]")
# m = p.match("Python")
p = re.compile("[a-z]", re.IGNORECASE)
m = p.match("Python")
print(m)

print()
print()


print("-" * 5,"MULTILINE 옵션", "-" * 5)
p = re.compile("^python\s\w+", re.MULTILINE) #\s문자열 \w공백문자
# MULTILINE이 없으면 첫줄만 출력됨
data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

print()
print("-" * 5, "VERBOSE", "-" * 5)

charref = re.compile(r'&[#](0[0-7)]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
&[#]                # 시작
(
0[0-7]+             # 8진수
| [0-9]+            # 10진수
| x[0-9a-fA-F]+     # 16진수
)
;
""", re.VERBOSE)



print()
print("-" * 5, "| 메타문자", "-" * 5)
p = re.compile("Crow|Servo")
m = p.search("CrowHello")
print(m)



print()
print("-" * 5, "^ 메타문자", "-" * 5)
p = re.compile("^Life")
m = p.search("Life is too short")
print(m)
m = p.search("My Life is too short")   #위에 ^이 무조건 첫번째 글자만 찾아오기에 none이 뜨는거임
print(m)



print()
print("-" * 5, "$ 메타문자", "-" * 5)
p = re.compile("short$")
m = p.search("Life is too short")
print(m)
m = p.search("Life is too short, you need python") #위에 $이 무조건 마지막 글자만 찾아오기에 none이 뜨는거임
print(m)



print()
print("-" * 5, "\\A \\Z 메타문자", "-" * 5)
data = """python one 00
life is too short 00
python two 00
you need python 00
python three 00"""

p = re.compile("^python\s\w+")
m = p.findall(data)
print("MULTILINE 미사용, ^ 검색 : {0}".format(m))

p = re.compile("\Apython\s\w+")
m = p.findall(data)
print("MULTILINE 미사용, \A 검색 : {0}".format(m))

p = re.compile("^python\s\w+", re.MULTILINE)
m = p.findall(data)
print("MULTILINE 미사용, ^ 검색 : {0}".format(m))

p = re.compile("\Apython\s\w+", re.MULTILINE)
m = p.findall(data)
print("MULTILINE 미사용, \A 검색 : {0}".format(m))

print()

p = re.compile("00$")
m = p.findall(data)
print("MULTILINE 미사용, $ 검색 : {0}".format(m))

p = re.compile("00\Z")
m = p.findall(data)
print("MULTILINE 미사용, \Z 검색 : {0}".format(m))

p = re.compile("00$",re.MULTILINE)
m = p.findall(data)
print("MULTILINE 미사용, $ 검색 : {0}".format(m))

p = re.compile("00\Z", re.MULTILINE)
m = p.findall(data)
print("MULTILINE 미사용, \Z 검색 : {0}".format(m))



print()
print("-" * 5, "\\b 메타문자", "-" * 5)
p =  re.compile(r"\bclass\b")
m = p.search("no class at all")
# m = p.search("no_class_at_all")
print(m)

print()
print("-" * 5, "()로 그룹만들기", "-" * 5)

data ="name: park     010-1234-5678, email: aaa@gmail.com"
p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
# p = re.compile(r"([0-9]{3}-[0-9]{3,4}-[0-9]{4})")
m = p.search(data)
print(m)

print("-" * 5, "그룹의 index 사용", "-" *5)
p = re.compile(r"(\w+)\s+\d+[-]\d+[-](\d+)")
m = p.search(data)
print(m.group(1), m.group(2))


print("-" * 5, "그룹의 이름 붙여서 사용", "-" *5)
p = re.compile(r"(?P<name>\w+)\s+\d+[-]\d+[-](?P<number>\d+)")
m = p.search(data)
print(m.group("name"), m.group("number"))



print()
print("-" * 5, "sub 메서드", "-" * 5)

p = re.compile("(blue|white|red)")
m = p.sub("color", "blue socks and red shoes")
print(m)

p = re.compile("(blue|white|red)")
m = p.sub("color", "blue socks and red shoes", count=1)
print(m)



print()
print("-" * 5, "greedy(탐욕적 수량자)", "-" * 5) # =====> *, +, {m, }

data = "<html><head><title>TITLE</title>"
size = len(data)
print("문자열 data의 길이 : {0}".format(size))

p = re.compile("<.*>")
m = p.match(data)
print(m)
print(m.span(), m.group())


print()
print("-" * 5, "lazy(게으른 수량자)", "-" * 5) # =====> *?, +?, {m, }?

p = re.compile("<.*?>")
m = p.match(data)
print(m)
print(m.span(), m.group())
