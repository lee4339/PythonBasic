# 문제 1) usecsv 모듈을 사용하여 popSeoul.csv 파일의 내용을 불러와서 화면에 내용을 출력
# for 문을 사용하여 한줄씩 출력

# 문제 2) usecsv 모듈을 사용하여 popSeoul.csv파일의 내용을 불러와서 popSeoul_copy.csv 파일로 복사하는 프로그램을 작성하세요.

# 문제 3) usecsv 모듈을 사용하지 않고 직접 csv 모듈을 사용하여 popSeoul.csv 파일을 읽어와서 popSeoul.copy2.csv 파일로 복사하는 프로그램을 작성하세요.

# import usecsv
# import csv
#
#
# print("-문제1-")
#
# usecsv_open = usecsv.open_csv('popSeoul.csv')
# print(usecsv_open)
#
# print("-문제2-")
# usecsv.write_csv('popSeoul_copy.csv', usecsv_open)
# print("저장완료")
#
# print("-문제3-")
#
# f = open('popSeoul.csv', 'r', encoding='UTF-8')
# csv_r = csv.reader(f)
# print(csv_r)
#
# csv_data = []
# for item in csv_r:
#     csv_data.append(item)
# print(csv_data)
# f.close()


###########################################################################
import re

# csv 모듈을 통해서 불러온 모든 데이터는 문자열 타입임
# 연산을 진행하려면 int(), float()을 사용하여 숫자 데이터로 변환
# csv 파일을 통해서 데이터를  불러오면 숫자 데이터에 쉼표가 붙어 있어 숫자로 변환 시 오류가 발생
# 정규 표현식을 사용하여 쉼표(,)를 제거하여 사용해야 함
# sub() 함수를 사용


i = '123'
j = '141,767'
print(int(i))
print(float(i))

# print(int(j))
# print(float(j))
j = re.sub(',','', j)

print(int(j))
print(float(j))

data = ["종로구","151,767","11,093","27,394"]
print("원본 데이터 : {0}".format(data))

# 파이썬의 정규표현식 모듈인 re를 사용하여 검색 패턴 생성
# 정규 표현식 \d 는 [0-9]와 같음
p = re.compile(r'\d')

con_data = []

# 리스트 data에서 각각의 요소를 하나씩 가져와서 변수 item에 저장
for item in data:
    # 생성된 패턴을 기준으로 문자열을 검색
    # 숫자 데이터가 있으면 
    if p.search(item):
        # re.sub() 를 사용하여 검색된 문자열을 지정한 문자열로 변경
        item = re.sub(',','', item)
        # 쉼표가 제거된 문자열 타입의 숫자데이터를 숫자타입으로 변경
        float_data = float(item)
        # 숫자 타입으로 변경된 데이터를 리스트 con_data에 추가
        con_data.append(float_data)
    # 숫자 데이터가 없으면 리스트 con_data에 데이터 추가
    else:
        con_data.append(item)

print("변환된 데이터 : {0}".format(con_data))





