print("-" * 5, "리스트와 반복문", "-" * 5)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
print(numbers[5])
print(numbers[6])
print(numbers[7])
print(numbers[8])
print(numbers[9])


print("-" * 5, "while을 사용한 리스트이 내용 출력", "-" * 5)
count = 0

while count < 10:
    print("number[{0}] : {1}".format(count, numbers[count]))
    count = count + 1

# 문제 6) list_a라는 빈 리스트를 생성하고 해당 리스트에 1 ~ 10까지의 데이터를 저장한 후 while문을 사용하여 리스트에 저장된 모든 숫자를 합하는 프로그램을 작성하세요.
print("-" * 5, "문제 6번", "-" * 5)
count = 0
list_a = []
while count < 10:
    count = count + 1
    list_a.append(count)

print(list_a)
print("list_a의 전체 합 : {0}".format(sum(list_a)))

total = 0
count = 0

while count < 10:
    total = total + list_a[count]
    print("total : {0}".format(total))
    count = count + 1