import re
import usecsv

#C:\programing\PythonBasic\workspace\class_e_python\PythonBasic\python0714\popSeoul.csv
# 위와 같이 해당 파일의 경로를 인식하지 못함
# 리눅스 및 맥 OS의 경우는 경로를 표시하는 문자를 /를 사용함
# 윈도우에서는 경로를 표시하는 문자를 \를 기본으로 사용함
# 문자열 안에서 \ 는 이스케이프 문자를 뜻함
# 경로를 표시하는 문자를 사용시 \\ 형태로 사용하여 경로를 표시해야함
# 파이썬에서 경로를 쉽게 표기하기 위해서 문자열 앞에 r 기호를 사용함

file_data = usecsv.open_csv(r'C:\programing\PythonBasic\workspace\class_e_python\PythonBasic\python0714\popSeoul.csv');
# print(file_data)

# 원본 csv 파일에서 데이터를 가져와서 숫자 데이터로 변경
# p = re.compile(r'[a-zA-Z가-힣!@#]')

# 변경된 데이터를 모두 저장할 리스트
# total = []
#
# for item_list in file_data:
#     con_data = []
#
#     for item in item_list:
#         if p.search(item):
#             con_data.append(item)
#         else:
#             item = re.sub(',','', item)
#             try:
#                 float_data = float(item)
#             except ValueError:
#                 float_data = item
#             con_data.append(float_data)
#     total.append(con_data)
# print(total)
print()

# 원본 csv 파일에서 데이터를 가져와서 숫자 데이터로 변경
con_data = usecsv.switch(file_data)
# print(con_data[:4])

i = con_data[1]
# print(i)

# rount() : 지정한 데이터를 반올림함, 2번째 매개변수를 소수점 몇번째 자리까지 표시할 것인지 설정
# 비율 공식 : 외국인 / 전체인구 * 100
# foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
# print(foreign)

# 전체 데이터에서 외국인의 비율을 모두 표시
# for i in con_data:
#     foreign = 0
#
#     try:
#         foreign = round(i[2]/ (i[1] + i[2]) * 100, 1)
#         print(i[0], foreign)
#     except:
#         pass


#외국 비율 정보가 포함된 2차원 리스트 생성
new = [
    ['구', '한국인', '외국인', '외국인 비율(%)']
]

for i in con_data:
    foreign = 0

    try:
        # 외국인 비율 계산
        foreign = round(i[2]/ (i[1] + i[2]) * 100, 1)
        # 외국인 비율이 3보다 큰 구의 정보만 new리스트에 저장
        if foreign > 3:
            data = [i[0], i[1], i[2], foreign]
            new.append(data)
            # new.append([i[0], i[1], i[2], foreign])
    except:
        pass

print(new)

usecsv.write_csv('foreign.csv', new)




