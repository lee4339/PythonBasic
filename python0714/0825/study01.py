import re

# 1. 숫자를 기반으로 검색 시 '123종로구'와 같이 숫자와 문자가 동시에 있을 경우 쉼표 제거 루틴이 동작하는 부분이 실행되어 에러가 발생함
data = ["123@","151,767","11,093","27,394", "", "!!@@##"]
print("원본 데이터 : {0}".format(data))

# 우리가 지정한 문자 형태가 있는지만 검색하는 형태로 변경
p = re.compile(r'[a-zA-Z가-힣!@#]')
con_data = []

for item in data:
    # 문자가 포함된 데이터는 리스트 con_data에 변경없이 추가
    if p.search(item):
        con_data.append(item)
    # 문자가 포함된 데이터가 아니면(숫자 + ,) 쉼표를 제거하는 루틴실행
    else:
        # 숫자,숫자  인 데이터에서 숫자 인 데이터로 변환
        item = re.sub(',', '', item)
        # 숫자 타입으로 변경 시 빈문자열은 오류가 발생하므로 예외처리를 통해서 프로그램이 멈추지 않도록 처리함
        try:
            # 문자열 타입인 숫자 데이터를 숫자 타입의 데이터로 변경
            float_data = float(item)
        except ValueError:
            float_data = item
        #     pass

        # 변경된 데이터를 리스트 con_data에 추가
        con_data.append(float_data)


print("변환된 데이터 : {0}".format(con_data))




