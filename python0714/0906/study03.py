import pandas as pd
import numpy as np

print('-' * 5, '판다스 사용하기', '-' * 5)

# 판다스 : 데이터 분석을 위해서 사용하는 모듈
# 데이터 오브젝트 : 데이터를 담고 있는 그릇, Series, DataFrame 이라고 하는 2가지 형태의 데이터 오브젝트가 존재함
# Series : 1차원 배열 형태, 인덱스를 기준으로 데이터 저장 됨
# DataFrame : 2차원 배열 형태, 인덱스와 컬럼을 기준으로 데이터가 저장

# index를 사용하여 원하는 데이터를 가져올 수 있음
# 슬라이싱 기법도 사용이 가능함
s1 = pd.Series([1, 3, 5, 7, 9])
print(s1)
print(s1[0])
print(s1[2:])

print()

# 딕셔너리 타입의 데이터를 판다스로 가공이 가능함
data = {'name' : ['mark', 'jane', 'chris', 'ryan'],
        'age' : [33, 22, 44, 42],
        'score' : [91.3, 83.4, 77.5, 87.7]}

df = pd.DataFrame(data)
print(df)

# DataFrame() : 판다스의 DataFrame 타입으로 데이터를 변환
# sum() : 특정 값의 합계를 구할 수 있음
# mean() : 특정 값들의 평균을 구할 수 있음
# head(크기) : DataFrame 타입의 앞쪽에 있는 데이터 확인, 지정한 크기만큼의 앞쪽의 데이터를 확인
# tail() : DataFrame 타입의 뒷쪽에 있는 데이터 확인, 지정한 크기만큼의 뒷쪽의 데이터를 확인

# 데이터가 row가 되고 위에 목록이 columns가 됨(?)

print('sum() : \n{0}'.format(df.sum()))
print('mean() : \n{0}'.format(df.mean(numeric_only=True)))  # numeric_only=True : 숫자인 부분만 연산하라
# print('age만 가져오기 : \n{0}'.format(df.age))
print('age만 가져오기 : \n{0}'.format(df['age']))



print('-' * 5, '판다스에서 csv 파일 사용하기', '-' * 5)

df = pd.read_csv('apt2.csv', encoding='utf-8')

# head(), tail()을 사용하여 데이터의 처음과 마지막 부분 가져오기
print(df.head(10))
print(df.tail())

# 원하는 컬럼의 데이터 가져오기
print(df.가격)
print(df.시군구)

# 조건별로 데이터 가져오기
print(df[df.면적 > 130])

# 면적이 130 초과인 데이터 프레임 중에서 가격만 출력하기
print(df.가격[df.면적 > 130])

# 조건을 추가하기 위해서 &와 | 를 사용할 수 있음
print(df.가격[(df.면적 > 130) & (df.가격 < 15000)])
print(df.가격[(df.면적 > 130) | (df.가격 < 15000)])