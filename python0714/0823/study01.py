import csv
print("-" * 5, "csv 파일 다루기", "-" * 5)

# csv 모듈
# 아나콘다를 설치 시 기본적으로 사용할 수 있는 모듈
# csv 파일을 읽고 쓰기가 가능한 모듈


# csv 파일을 기존의 텍스트 파일 데이터를 가져오듯이 불러오면 원하지 않는 데이터도 같이 가져옴
# 필요없는 부분에 대한 파싱 처리가 필요함

print("-" * 3, "csv 모듈 X", "-" * 3)
f = open("a.csv", "r", encoding="UTF-8-sig")
# sig는 signature의 약자이며 +"-sig" 가 붙으면서 "\ufeff"는 문자열이 아닌 인코딩 정보로 인식하게 되어 해당 문자는 표시되지 않게됨
line = f.readlines()
f.close()

print(line)

list_tmp = []

for item in line:
    item = item[:-1]
    list_tmp.append(item.split(','))

# print(list_tmp)

for item in list_tmp:
    print(item)
# csv 모듈을 사용하면 필요한 부분의 데이터만 읽어오거나 쓰기가 가능함

# reader(파일객체, 구분기호) : 지정한 csv파일의 내용을 읽어옴
# --> 내용을 출력 시 for문을 사용하여 내용을 출력
# --> reader() 사용 시 파일을 열고 있는 상태에서 사용해야 함
#     파일을 닫고 실행 시 오류가 발생함.
# 구분기호 : delimiter=기호, reader()에서는 , 가 기본 기호임

# writer(파일객체, 구분기호, 옵션) : 지정한 csv파일에 내용을 쓰기
# 구분기호 : delimiter=기호, writer()에서는 반드시 입력해야 함
# csv객체.writerows(리스트) : 실제로 csv파일에 내용을 쓰기
# csv 모듈을 통해서 데이터 쓰기를 진행할 경우 데이터는 2차원 리스트 방식으로 되어 있어야 함

reader = [] # csv.reader()을 사용하여 가져온 데이터를 저장할 리스트

print("-" * 3, "csv 모듈 O", "-" * 3)
f = open("a.csv", "r", encoding="UTF-8-sig")
csv_obj = csv.reader(f)
print(csv_obj)

# 생성된 csv객체는 파일을 닫기 전에 사용해야 함
for item in csv_obj:
    print(item)
    # csv 객체에 저장된 데이터를 리스트에 저장
    reader.append(item)

f.close()
# 파일이 닫힌 후 csv객체를 사용하면 오류가 발생함
# for item in csv_obj:
#   print(item)

# 리스트에 저장된 내용 출력하기
print(reader)
for item in reader:
    print(item)

print()

print("-" * 5, "writer()을 사용하여 csv 파일 쓰기", "-" * 5)

# 그냥 파일 쓰기 모드로 열고 csv 모듈로 데이터를 쓰면 한 라인씩 빈 라인이 발생함
# 파일을 열때 newline='' 옵션을 추가해야 함
f = open('b.csv', 'w', encoding='UTF-8', newline='')
# csv 모듈을 통해서 지정한 csv파일에 쓰기 방식 설정
csv_obj = csv.writer(f, delimiter=',')
# 리스트에 저장된 데이터를 csv파일에 쓰기 실행
csv_obj.writerows(reader)
f.close()

