print("-"*5, "튜플 사용하기", "-"*5)

t1 = () # 빈 튜플
t2 = (1, ) # 튜플의 요소가 1개만 있을 경우 반드시, 사용
t3 = (1, 2, 3)
t4 = 1, 2, 3 # 튜플 선언 시 ()를 생략해도 됨
t5 = ('a', 'b', (1, 2)) # 2차원 튜플

print("튜플 t1 : {0}".format(t1))
print("튜플 t2 : {0}".format(t2))
print("튜플 t3 : {0}".format(t3))
print("튜플 t4 : {0}".format(t4))
print("튜플 t5 : {0}".format(t5))

print("-" * 20)

tuple1 = (10, 20, 30, 40, 50)
list1 = [10, 20, 30, 40, 50]

print("튜플 tuple1 : {0}".format(tuple1))
print("리스트 list1 : {0}".format(list1))

print("리스트의 마지막 index의 값 : {0}".format(list1[4]))
print("튜플의 마지막 index의 값 : {0}".format(tuple1[-1]))

print("리스트에서 슬라이싱 사용 : {0}".format(list1[1:3]))
print("듀플에서 슬라이싱 사용 : {0}".format(tuple1[2:]))

list1[2] = 300
print("리스트의 2번 index 값 수정 : {0}".format(list1[2]))

#튜플은 읽기 전용이기 때문에 데이터의 수정 및 삭제가 불가능함
#tuple1[2] = 300
#print("튜플의 2번 index 값 수정 : {0}".format(tuple1[2]))
#del tuple1[1]

size = len(tuple1)
print("튜플 tuple1의 길이는 : {0}".format(size))


#############################################################
print("\n\n","-"*5, "튜플의 언산", "-"*5)

tuple2 = (60, 70, 80, 90, 100)
tuple_result = tuple1 + tuple2
print("tuple1 + tuple2 = {0}".format(tuple_result))

tuple_result = tuple2 * 2
print("tuple2 * 2 = {0}".format(tuple_result))

print(tuple2)
# list(튜플) : 튜플의 데이터를 리스트로 변환, 새로운 리스트로 생성
# tuple(리스트) : 리스트의 데이터를 튜플로 변환,
t2l = list(tuple2)
print(t2l)

t2l[0] = 600
print(t2l)

l2t = tuple(t2l)
print(l2t)