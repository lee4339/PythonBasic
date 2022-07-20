print("-"*5, "리스트 사용하기", "-"*5)
#변수는 데이터를 1개만 저장할 수 있음
a = 10
print("변수 a의 값 : {0}".format(a))
#변수에 새로운 데이터를 저장 시 기존 데이터는 삭제
a = 20
print("변수 a의 값 : {0}".format(a))
#리스트 선언
list_a = [1, 2, 3, 4, 5]
print("리스트 list_a의 값 : {0}".format(list_a))


print("-"*3, "리스트 list_a에 저장된 각각의 값", "-"*3)
print("index : 0, value : {0}".format(list_a[0]))
print("index : 1, value : {0}".format(list_a[1]))
print("index : 2, value : {0}".format(list_a[2]))
print("index : 3, value : {0}".format(list_a[3]))
print("index : 4, value : {0}".format(list_a[4]))

# 지정한 index에 있는 데이터 변경
list_a[2] = 30
print("index : 2, value : {0}".format(list_a[2]))
print("리스트 list_a의 전체값 : {0}".format(list_a))
print()

#파이썬의 변수는 데이터 타입을 변수에 데이터가 저장되는 시점에 데이터 타입을 확인함
#변수를 선언만 하고 데이터를 저장하지 않을 경우 해당 변수의 데이터 타입을 알 수 없음
#변수를 선언 시 사용하고자 하는 데이터 타입의 빈값을 입력하여 해당 변수의 데이터 타입을 지정하고 나중에 사용함
a = [] #빈 리스트 선언
b = [1, 2, 3]
c = ["Life", "is", "too", "short"]
#파이썬의 변수는 변수 선언 시 데이터 타입을 확인하지 않고, 데이터가 저장될 때 데이터 타입을 확인하기 때문에 모든 데이터 타입을 저장할 수 있음
#파이썬의 리스트의 요소는 데이터 타입을 구분하지 않음
d = [1, 2, "Life", "is"] #숫자와 문자열을 모두 저장하는 리스트

e = [1, 2, ["Life", "is"]] #리스트의 요소로 리스트를 저장함
print("빈 리스트 a : {0}".format(a))
print("숫자를 저장한 리스트 b : {0}".format(b))
print("문자열 리스트 c : {0}".format(c))
print("숫자와 문자열을 저장한 리스트 d : {0}".format(d))
print("리스트의 요소로 리스트를 저장한 리스트 e : {0}".format(e))

print(e[0])
print(e[2])
print(e[2][0])

print(e[-1][-1])

############################################################################

print("\n\n", "-"*5, "슬라이싱 사용하기", "-"*5)
list_b = [10, 20, 30, 40, 50]
print(list_b)
print(list_b[1:3])
print(list_b[:3])
print(list_b[1:])
print(list_b[:])

############################################################################

print("\n\n", "-"*5, "리스트 연산하기", "-"*5)
list_c = [10, 20, 30]
list_d = [40, 50, 60]

#리스트를 + 연산자로 연산 시 2개의 리스트를 하나의 큰 리스트로 변경
list_result = list_c + list_d
print(list_result)

#리스트를 * 연산자로 연산 시 하나의 리스트가 여러번 반복된 큰 리스트로 변경
list_result = list_c * 3
print(list_result)

############################################################################

print("\n\n", "-"*5, "리스트 길이 구하기 len()", "-"*5)
list_e = [10, 20, 30, 40, 50]
print("리스트 list_e의 길이 : {0}".format(len(list_e)))

############################################################################

print("\n\n", "-"*5, "리스트에 요소 추가/삭제", "-"*5)
list_f = [10, 20, 30, 40, 50]
print("원본 리스트 list_f : {0}".format(list_f))

list_f.append(60)
list_f.append(70)
list_f.append(80)
print("append 사용 후 list_f : {0}".format(list_f))

del list_f[0]
del list_f[1]
print("del 사용 후 list_f : {0}".format(list_f))

list_f.pop()
list_f.pop()
list_f.pop()
print("pop 사용 후 list_f : {0}".format(list_f))

list_f.insert(1, 45)
list_f.insert(0, 35)
list_f.append(60)
list_f.insert(-1, 55)
print("insert 사용 후 list_f : {0}".format(list_f))

############################################################################

print("\n\n", "-"*5, "리스트 정렬", "-"*5)
list_g = [3, 34, 21, 17, 10, 45]
print("원본 리스트 list_g : {0}".format(list_g))

list_g.sort()
print("sort 사용 후 list_g : {0}".format(list_g))

list_h = [3, 34, 21, 17, 10, 45]
print("원본 리스트 list_h : {0}".format(list_h))
list_h.reverse()
#reverse()는 역정렬이 아닌, 기존의 리스트의 순서를 반대로 뒤집어 출력함
print("reverse 사용 후 list_h : {0}".format(list_h))
#역정렬을 하려면 sort를 사용하여 먼저 정렬하고 reverse를 사용하여 순서를 변경해야함


############################################################################

print("\n\n", "-"*5, "index, count, remove", "-"*5)
list_i = [10, 20, 30, 40, 10, 20, 30, 50, 60, 80, 90, 10]
print("50의 위치는 : {0}".format(list_i.index(50)))
#print("70의 위치는 : {0}".format(list_i.index(70)))
print("30의 위치는 : {0}".format(list_i.index(30)))

print("리스트 list_i에 10의 갯수는 : {0}".format(list_i.count(10)))

print("원본 리스트 list_i : {0}",format(list_i))
print("리스트 list_i에서 90 삭제")
list_i.remove(90)
print("remove 사용 후 list_i : {0}".format(list_i))


print("\n\n", "-"*5, "반복문에서 count, remove", "-"*5)
print("원본 리스트 list_i : {0}",format(list_i))
count = list_i.count(10)

while count > 0:
    list_i.remove(10)
    print("remove 사용 후 list_i : {0}".format(list_i))
    count = list_i.count(10)


print("\n\n", "-"*5, "extend", "-"*5)
list_j = [10, 20, 30]
list_k = [40, 50, 60]
list_l = [10, 20, 30]
list_m = [40, 50, 60]
list_n = list_j + list_k
print("list_j : {0}, list_k : {1}".format(list_j, list_k))
print("list_j + list_k : {0}".format(list_n))
print("list_j : {0}, list_k : {1}".format(list_j, list_k))
#새로생성
print()

print("list_l : {0}, list_m : {1}".format(list_l, list_m))
list_l.extend(list_m)
print("list_l.extend(list_m) : {0}".format(list_l))
print("list_l : {0}, list_m : {1}".format(list_l, list_m))
#원본에 추가하여 수정

print("\n\n", "-"*5, "문자열 함수 split", "-"*5)
#split() : 문자열 내에 존재하는 문자를 기준으로 문자열을 분해하여 리스트로 변환하는 명령
origin = "abc$def$ghi$jklmn$opqr$stuv$wxyz"
print("원본 문자열 : {0}".format(origin))
print(origin[0:3])
print(origin[4:7])
print(origin[8:11])
print(origin[12:17])
print(origin[18:22])
print(origin[23:27])
print(origin[28:])

split_list = origin.split("$")
print(split_list)













