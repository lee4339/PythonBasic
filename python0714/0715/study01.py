print("-"*5, "문자열 사용하기", "-"*5)
a = "Life is too short, You need Python"
print(a)
print(a[0])
print(a[12])
print(a[-1]) #역순

#############################################################

print()
print("-"*5, "문자열 슬라이싱", "-"*5)
a = "Life is too short, You need Python"
#a[시작번호:끝번호] ==> 인덱스 위치지정
print(a[0:4]) #0번 인덱스부터 4번 인덱스까지의 값을 가지고 옴

#a[ :끝번호] ==> 맨 처음부터(0번 인덱스부터 시작 ~ 끝번호까지)
print(a[:15])

#a[시작번호: ] ==> 맨 끝까지(시작번호부터 시작 ~ 마지막까지)
print(a[15:])

#[ : ] ==> 맨 처음부터 맨 끝까지(0번 인덱스부터 ~ 마지막 인덱스까지)
print(a[:])

#############################################################

print()
print("-"*5, "문자열 포맷팅", "-"*5)
f = "I eat %d apples." %3  # %d 정수(int) 3을 삽입
print(f)

number = 3
f = "I eat %d apples." %number    # 변수(int) 삽입
print(f)

f = "I eat %s apples." %"five"   # %s 문자열(str) "five" 삽입
print(f)

#############################################################

print()
print("-"*5, "자리수 채우기", "-"*5)
f = "hi jane"
print(f)

f = "%s jane" %"hi"
print(f)

f = "%10s jane" %"hi"   #hi로부터 오른쪽으로 부터 10칸 사용하고 ..
print(f)

f = "%-10s jane" %"hi"   #hi로부터 왼쪽으로 부터 10칸 사용하고 ..
print(f)

d = "%d" % 10
print(d)

d = "%4d" % 10
print(d)

d = "%-4d" % 10
print(d)

d = "%04d" % 10  # +- --> 오른쪽, 왼쪽 공백 0 --> 빈칸을 채울 문자 4 --> 확보할 칸의 수 d --> 출력할 데이터 방식
print(d)

fl = "%f" %3.14  # 실수
print(fl) # 기본적으로 소수점 뒤에 6자까지 출력

fl = "%.2f" %3.14 # .2 소수점 뒤 2자리까지 출력
print(fl)

#############################################################

print()
print("-"*5, "문자열 포맷팅 다른 방식", "-"*5)
#기존형식
str1 = "나의 이름은 %s입니다, 나이는 %d입니다." %("홍길동", 30)
print(str1)

#문자열.format()방식 {0, 1, 2, 3.....} .format(0, 1, 2, 3 ....에 넣을 값)
str2 = "나의 이름은 {0}입니다, 나이는 {1}입니다.".format("홍길동", 30)
print(str2)

#포멧 내에서 변수 설정
str3 = "나의 이름은 {name}입니다, 나이는 {age}입니다.".format(age = 30, name = "홍길동")
print(str3)

#변수 설정 후
name = "홍길동"
age = 30
str4 = f"나의 이름은 {name}입니다, 나이는 {age}입니다."
print(str4)

#############################################################

print()
print("-"*5, "문자열 함수 사용하기", "-"*5)
str = "Life is too short, You need Python"

print("문자열 길이 출력하기 len()")
length = len(str)
print("변수 str의 길이는 : {0} 입니다.".format(length))

print()

print("문자에 포함된 문자 수 출력하기 count()")
count = str.count('o')
print("변수 str에 포함된 문자 o의 갯수 : {0}".format(count))

#############################################################

print()
print("-"*5, "find()와 index()", "-"*5)
str = "Python is the best choice"

print("문자에 포함된 문자 검색 find()") # --> 있으면 문자가 처음 나온 위치 반환, 없으면 -1 출력
num = str.find('b')
print("변수 str에 'b'가 있는 위치 : {0}".format(num)) # 문자열(best)로도 검색가능 --> best 검색시 제일 첫 문자 위치 반환
num = str.find(' ')
print("변수 str에 ' '가 있는 위치 : {0}".format(num)) # 제일 처음 ' '이 있는 위치
num = str.find('k')
print("변수 str에 'k'가 있는 위치 : {0}".format(num)) # 없는 문자열은 -1 출력

print()

print("문자에 포함된 문자 검색 index()") # --> 있으면 find()와 같이 문자 위치 반환, 없으면 오류
num = str.index('best')
print("변수 str에 'b'가 있는 위치 : {0}".format(num)) # 제일 첫 문자 위치 반환
num = str.index(' ')
print("변수 str에 ' '가 있는 위치 : {0}".format(num)) # 제일 처음 ' '이 있는 위치
#num = str.index('k')
#print("변수 str에 'k'가 있는 위치 : {0}".format(num)) # 오류

#############################################################

print()
print("-"*5, "upper()와 lower()", "-"*5)
h = "Python Is The Best Choice"
print(h.upper()) #소문자를 대문자로 변환
print(h.lower()) #대문자를 소문자로 변환
# upper, lower은 DB, 검색에 사용됨

#############################################################

print()
print("-"*5, "join()과 strip()", "-"*5)
print(",".join('abcd'))  #문자열 삽입
join_str = ","
print(join_str.join("abcdefg"))

print()

h = "   hi   "   #양쪽 공백
print(h)
print(h.strip()) #양쪽에 있는 연속된 공백 삭제
print(h.rstrip()) #가장 오른쪽에 있는 연속된 공백 삭제
print(h.lstrip()) #가장 왼쪽에 있는 연속된 공백 삭제

#############################################################

print()
print("-"*5, "replace()와 split()", "-"*5)
re = "오늘은 초복 입니다."
print(re)

re = re.replace("오늘은", "내일은")
print(re)

re = re.replace("초복", "중복")
print(re)

re = re.replace("중복", "") #문자열을 지울 수도 있음
print(re)






