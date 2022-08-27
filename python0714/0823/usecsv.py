import csv, re

def open_csv(file_name):
    f = open(file_name, 'r', encoding='UTF-8')

    csv_reader = csv.reader(f)
    read_data = []

    for item in csv_reader:
        read_data.append(item)

    f.close()

    return read_data

def write_csv(file_name, write_data_list):
    f = open(file_name, 'w', encoding='UTF-8', newline='')

    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerows(write_data_list)

    f.close()



# 연산이 가능한 숫자 데이터로 변환해주는 변수
# data_list : 문자열 타입의 숫자 데이터가 포함되어 있는 데이터
def switch(data_list):
    # 변환된 전체 데이터가 저장될 리스트 변수(2차원 리스트)
    total = []

    # 원본 데이터가 2차원 리스트 형태로 구성되어 있어서 2중 for문을 사용하여 모든 데이터를 확인함
    for item_list in data_list:
        # 각각의 변환된 데이터가 저장될 리스트 변수(1차원 리스트)
        con_data = []

        for item in item_list:
            # 문자가 포함된 데이터인지 확인
            if re.search(r'[a-zA-Z가-힣!@#]', item):
                # 문자 포함된 데이터는 그냥 리스트에 저장
                con_data.append(item)
            # 숫자 데이터일 경우 ,제거
            else:
                # 쉼표 제거
                item = re.sub(',', '', item)
                # 연산이 가능하도록 숫자 데이터로 변환
                try:
                    float_data = float(item)
                except ValueError:
                    float_data = item
                # 변환된 숫자 데이터를 리스트에 저장
                con_data.append(float_data)

        # 변환된 모든 데이터를 저장
        total.append(con_data)
    return total
