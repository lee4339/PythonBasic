print("-"*5, "딕셔너리 사용하기", "-"*5)

dic = {"name" : "pey", "phone" : "01012347896", "birth" : "0721"}
print(dic)

# 딕셔너리를 사용하여 지정한 키의 데이터 출력
print(dic["name"])
# 딕셔너리를 사용하여 지정한 키에 데이터 저장
dic["name"] = "hong"
print(dic["name"])


##########################################################################
print("\n\n", "-"*5, "딕셔너리의 데이터 추가/삭제", "-"*5)

car = {"name" : "토레스", "type" : "SUV", "size" : "중형"}
print(car)
print("내가 구입한 차는 {0}이고, 차종은 {1}이다.".format(car["name"], car["type"]))


#기존의 딕셔너리에 데이터를 추가
car["CC"] = "1500"
car["gas"] = "가솔린"
car["color"] = "흰색"
car["co"] = "쌍용"
car["price"] = "2,740"

print("\n\n내가 구입한 차는 {0}에서 개발한 {1}이고, {2}CC의 {3}을 연료로 하는 {4} 크기의 {5} 이다.".format(car["co"], car["name"], car["CC"], car["gas"], car["size"], car["type"]))

# 기존의 딕셔너리에서 데이터를 삭제
del car["price"]
print(car)

# 딕셔너리 사용 시 주의점
# key 는 중복될 수 없음
# value는 중복 가능함

info1 = {"name" : "홍길동", "age" : 24, "birth" : "0721", "birth" : "0701"}
print(info1)

info2 = {"name" : "임꺽정", "age" : 30, "birth" : "0721", "regdate" : "0721"}
print((info2))



##########################################################################
print("\n\n", "-"*5, "딕셔너리의 데이터 추가/삭제", "-"*5)
car2 = {"name" : "토레스", "type" : "SUV", "size" : "중형", "gas" : "가솔린", "price" : "2,740", "cc" : "1,500"}

print("-" * 5, "keys()", "-" * 5)
# kyes() : 딕셔너리가 가지고 있는 모든 키를 반환
# list()를 사용하여 리스트로 변경하여 사용

car_keys = car2.keys()
print(car_keys)

car_key_list = list(car_keys)
print(car_key_list)
print(car_key_list[0])
print(car_key_list[1])
print(car_key_list[2])
print(car_key_list[3:])


print("-" * 5, "values()", "-" * 5)
# values() : 딕셔너리가 가지고 있는 모든 값을 반환
# list() 를 사용하여 리스트로 변경하여 사용
car_values = car2.values()
print(car_values)

car_value_list = list(car_values)
print(car_value_list)
print(car_value_list[0])
print(car_value_list[1])
print(car_value_list[2:4])


print("-" * 5, "items()", "-" * 5)
# items() : 딕셔너리가 가지고 있는 모든 key와 value를 반환
# list() 를 사용하여 리스트로 변경하여 사용
# 리스트의 각각의 요소가 모두 튜플로 이루어져 있음

car_items = car2.items()
print(car_items)

car_item_list = list(car_items)
print(car_item_list)
print(car_item_list[0])
print(car_item_list[2])
print(car_item_list[3:])
print(car_item_list[0][0])
print(car_item_list[0][1])



##########################################################################
print("\n\n", "-"*5, "clear 사용", "-"*5)

print("원본 딕셔너리 car2 : {0}".format(car2))
car2.clear()
print("clear 사용 후 car2 : {0}".format(car2))

car3 = {"name" : "토레스", "type" : "SUV", "gas" : "가솔린", "price" : "2,740"}
print("원본 딕셔너리 car3 : {0}".format(car3))
print("딕셔너리 car3에 name이 있다? : {0}".format("name" in car3))
print("딕셔너리 car3에 size이 있다? : {0}".format("size" in car3))



##########################################################################
print("\n\n", "-"*5, "get() 사용", "-"*5)

print("원본 딕셔너리 car3 : {0}".format(car3))

print("['key']방식으로 출력 : {0}".format(car3["name"]))
print("get('key')방식으로 출력 : {0}".format(car3.get("name")))

print("----- 지정한 키가 없을 경우 -----")
# 지정한 키가 없을 경우 오류가 발생
# print("car3['size'] 출력 : {0}".format(car3["size"]))   ---> 오류
# 지정한 키가 없을 경우 None을 출력
print("car3.get('size') 출력 : {0}".format(car3.get("size")))  # ---> None


print("-"*5, "get() 사용하여 기본값 출력", "-"*5)
print("딕셔너리 car3에 key가 있을 경우 : {0}".format(car3.get("type", "기본값")))
print("딕셔너리 car3에 key가 없을 경우 : {0}".format(car3.get("size", "기본값")))
