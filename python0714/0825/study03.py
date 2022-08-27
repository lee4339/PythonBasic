import re
import usecsv

file_data = usecsv.open_csv('aptapt.csv')

apt_data = usecsv.switch(file_data)
# print(apt_data[:3])

# 전체 아파트 정보 중 5개만 가져오기
# 시군구 정보, 단지명, 거래가 출력
# for item in apt_data[:6]:
#     print(item[0], item[4], item[8])


new_list = []

# 강원도에서 120m^2 이상이고, 3억원 이하인 아파트 검색
# 0, 4, 5, 8 번 인덱스 사용
for item in apt_data:
    try:
        if item[5] > 120 and item[8] <= 30000 and re.match('강원도', item[0]):
            print(item[0], item[4], item[5], item[8])
            new_list.append([item[0], item[4], item[5], item[8]])
    except:
        pass

usecsv.write_csv("apt.csv", new_list)

print('\n' + '-' * 5, '아파트 정보 출력 완료', '-' * 5)




