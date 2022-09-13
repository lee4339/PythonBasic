import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('apt2.csv')

# 지정한 컬럼만 출력하기
print(df[['시군구', '단지명', '면적', '가격']])

# 원하는 크기 만큼의 데이터만 가져오기
print(df.loc[:10, ['시군구', '단지명', '면적', '가격']])

# 조건식을 사용하여 데이터 가져오기
print(df['면적'] > 130)

print(df[df['면적'] > 130])

print(df.가격[(df.면적 > 130) | (df.가격 < 15000)])

print(df.loc[: , ['단지명', '가격']][df.가격 > 40000])

# 정렬하기
# sort_values(by = "열이름", ascending = True|False)
print(df.sort_values(by='단지명', ascending=False)['단지명'])
print()
print(df.sort_values(by='가격').loc[:, ['가격', '단지명']])

# 가격이 4억이 넘고 면적이 넓은 순서로 정렬
print(df[df.가격 > 40000].sort_values(by='면적', ascending=False).loc[:, ['가격', '면적', '시군구']])


# 특정 문자를 포함하는 열 추출
# df.검색할열.str.find('검색어') : 검색어가 포함되어 있는 열의 index를 출력, 없으면 -1 출력
print(df.시군구.str.find('강릉)'))
print(df[df.시군구.str.find('강릉') > -1])

# 강릉이 포함된 데이터의 평균값
df_mean = df[df.시군구.str.find('강릉') > -1]
print(df_mean.mean(numeric_only=True))