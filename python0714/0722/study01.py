print("-" * 5, "bool 자료형", "-" * 5)

a = True
b = False

print(type(a))
print(type(b))

print(1 == 1)
print(2 > 1)
print(2 < 1)

print("-" * 5, "자료형의 참과 거짓", "-" * 5)

print("빈 문자열 : {0}".format(bool("")))
print("공백 문자열 : {0}".format(bool(" ")))
print("문자열 a : {0}".format(bool("a")))
print("숫자 0 : {0}".format(bool(0)))
print("숫자 양수 100 : {0}".format(bool(100)))
print("숫자 음수 -5 : {0}".format(bool(-5)))
print("실수 0.0 : {0}".format(bool(0.0)))
print("실수 0.5 : {0}".format(bool(0.5)))
print("실수 -0.5 : {0}".format(bool(-0.5)))
print("None : {0}".format(bool(None)))

list_a = []
list_b = [1, 2, 3]
tuple_a = ()
tuple_b = (1, 2, 3)
dic_a = {}
dic_b = {"name" : "aaa"}
set_a = set()
set_b = set("aaa")
print("빈 리스트 : {0}".format((bool(list_a))))
print("리스트 [1, 2, 3] : {0}".format((bool(list_b))))
print("빈 튜플 : {0}".format((bool(tuple_a))))
print("튜플 (1, 2, 3) : {0}".format((bool(tuple_b))))
print("빈 딕셔너리 : {0}".format((bool(dic_a))))
print("딕셔너리 dic_b : {0}".format((bool(dic_b))))
print("빈 집합 : {0}".format((bool(set_a))))
print("집합 set('aaa') : {0}".format(bool(set_b)))



#####################################################################3
print("\n\n", "-" * 5, "변수", "-" * 5)

c = [10, 20, 30]
print("리스트 c : {0}".format(c))
print("리스트 c의 주소 : {0}".format(id(c)))
print("리스트 c의 주소 %x" % id(c))


print("-" * 5, "변수 선언하기", "-" * 5)

#전개표현법
d, e = ("python", "life")
print("변수 d : {0}".format(d))
print("변수 e : {0}".format(e))

(f, g) = "python", "life"
print("변수 f : {0}".format(f))
print("변수 g : {0}".format(g))

[h, i] = ["python", "life"]
print("변수 h : {0}".format(h))
print("변수 i : {0}".format(i))



#################################################################
print("\n\n", "-" * 5, "스왑 사용하기", "-" * 5)

j = 100
k = 200
t = 0
print("변수 j : {0}". format(j))
print("변수 k : {0}". format(k))
t = j
j = k
k = t
print("변수 j : {0}". format(j))
print("변수 k : {0}". format(k))


print("-" * 5, "파이썬에서의 스왑 ", "-" * 5)
j = 100
k = 200
print("변수 j : {0}". format(j))
print("변수 k : {0}". format(k))

j, k = k, j
print("변수 j : {0}". format(j))
print("변수 k : {0}". format(k))