print("파이썬 프로그램 시작하기.")
########################################################
print("변수 사용하기")
a = 123
print(a)

a = 1000
print(a)

a = 2000
print(a)

a = -1000
print(a)

a = 3.14
print(a)

a = 0o100
print(a)

a = 0xff
print(a)

########################################################
print("-" * 5, "연산자 사용하기", "-" * 5) # "-" * 5 는 -를 5번쓰겠다.

a = 10
b = 20
c = a + b
print(c)

c = a - b
print(c)

c = a * b
print(c)

c = a ** 3
print(c)

c = a / 3
print(c)

c = a // 3  #소수점자리는 버리고 몫만 가져옴
print(c)

c= a % 3
print(c)

########################################################
print("-" * 5, "문자열 사용하기", "-" * 5)
d = 'hello "world"'
print(d)

d = "hello 'world'"
print(d)

e = "Life " \
    "is " \
    "too " \
    "short," \
    " You " \
    "need " \
    "Python"
print(e)

f = """Life 
is 
 too 
  short,
   You 
    need
     Python"""
print(f) #"""()""" 안에 문자를 마음에 대로 나열가능

g = 'Life ' \
    'is ' \
    'too ' \
    'short, ' \
    'You ' \
    'need ' \
    'Python'
print(g)

g = '''Life 
is 
too 
short, 
You 
need 
Python'''
print(g) #'''()''' 안에 문자를 마음에 대로 나열가능

h = "python's favorite food is perl"
print(h)

h = 'python\'s favorite food is perl'
print(h)

# 이스케이프 문자
# 문자열 내에서 특수한 기능을 하는 문자를 뜻한다.
# \n : 개행문자, 줄바꿈 문자, 엔터키를 누른 것과 동일한 효과
# \t : 탭 문자, 탭키를 누른 것과 동일한 효과
# \\ : 문자로써의 \를 출력하기 위한 것
# \" : 문자로써의 "를 출력하기 위한 것
# \' : 문자로써의 '를 출력하기 위한 것
h = "pythons \"favorite\" food is perl"
print(h)

h = "pythons \\favorite \\food is perl"
print(h)

h = "pythons \nfavorite \nfood is perl"
print(h)

########################################################
print("-" * 5, "문자열 연산", "-" * 5)
i = "오늘은 파이썬 "
j = "첫 강의 날입니다."
print(i)
print(j)
k = i + j
print(k)

l = "내일은 불금"
m = "!!"
n = l + m * 5
print(n)

print(len(n)) # len() 문자열 길이를 구해주는 함수이다.