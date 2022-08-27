import re
import usecsv

print('-' * 5, '내가 구입할 아파트 정보 찾기 프로그램', '-' * 5)

local = input("지역을 선택하세요 : ")
price = input("가격을 설정하세요(만원 단위) : ")
price = int(price)
size = input("크기를 설정하세요 : ")
size = int(size)

file_data = usecsv.open_csv('aptapt.csv')
apt_info = usecsv.switch(file_data)

my_apt_info = []

for item in apt_info:
    try:
        if re.match(local, item[0]) and size >= item[5] and price >= item[8]:
            print(item[0], item[4], item[5], item[8])
            my_apt_info.append([item[0], item[4], item[5], item[8]])
    except:
        pass

file_name = input("생성할 파일 이름을 입력하세요 : ")
file_name = file_name + ".csv"
usecsv.write_csv(file_name, my_apt_info)

print('\n' + '-' * 5, '아파트 정보 출력 완료', '-' * 5)



