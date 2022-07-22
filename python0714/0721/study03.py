print("-"*5, "집합(set) 사용하기", "-"*5)

s1 =  set([10, 20, 30])
print(s1)

s2 = set("hello")
print(s2)

# 집합(set)형태로 만들어진 데이터를 일반적인 형태로 사용하려면 list()를 사용하여 리스트로 변경하여 사용해야 함

s3 = set([10, 20, 30, 40, 50, 60])
s4 = set([40, 50, 60, 70, 80, 90])

print("집합 s3 : {0}".format(s3))
print("집합 s4 : {0}".format(s4))

print("\n-----교집합-----")
result = s3 & s4
print("s3 & s4 : {0}".format(result))
print("s3 : {0} \ns4 : {1}".format(s3, s4))
print(s3.intersection(s4))
#원본은 그대로 새로운 결과를 만든 것 원본 값을 변경하는 것이 아님

print("\n-----합집합-----")
result = s3 | s4
print("s3 | s4 : {0}".format(result))

print("\n-----차집합-----")
result = s3 - s4
print("s3 - s4 : {0}".format(result))




print("\n\n", "-"*5, "add, update, remove", "-"*5)

s5 = set([10, 20, 30])
print("원본 집합 s5 : {0}".format(s5))

s5.add(40)
s5.add(50)
s5.add(40) #중복값 제거됨
print("add 사용 후 s5 : {0}".format(s5))


s5.update([60,70,80])
print("update 사용 후 s5 : {0}".format(s5))

s6 = set([90, 100])
s5.update(s6)
print("update 사용 후 s5 : {0}".format(s5))

s5.remove(100)
s5.remove(10)
print("remove 사용 후 s5 : {0}".format(s5))