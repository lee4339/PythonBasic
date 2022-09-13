import numpy as np
import pandas as pd

print("-" * 5, '판다스', "-" * 5)

# Series 생성방법
# 1차원 리스트로 생성
# numpy의 1차원 배열로 생성
# pandas.Series(1차원리스트, index=[리스트])

# 1차원 리스트로 생성
print("-" * 5, '리스트로 Series 생성', "-" * 5)
sr1 = pd.Series([17000, 18000, 19000, 10000])
sr2 = pd.Series([17000, 18000, 19000, 10000], index=['치즈피자', '페퍼로니피자', '콤비네이션피자', '치킨텐더'])
print('sr1 : \n{0}\n{1}'.format(sr1, type(sr1)))
print('sr2 : \n{0}\n{1}'.format(sr2, type(sr2)))


print("-" * 5, '넘파이 배열로 Series 생성', "-" * 5)
arr = np.array([17000, 18000, 19000, 10000])
print("arr : \n{0}\n{1}".format(arr, type(arr)))

sr3 = pd.Series(arr)
sr4 = pd.Series(arr, index=['치즈피자', '페퍼로니피자', '콤비네이션피자', '치킨텐더'])
print('sr3 : \n{0}\n{1}'.format(sr3, type(sr3)))
print('sr4 : \n{0}\n{1}'.format(sr4, type(sr4)))

# Series의 값과 인덱스 출력하기 위해서 values, index가 존재
print("Series sr4의 values : {0}".format(sr4.values))
print("Series sr4의 index : {0}".format(sr4.index))

print("\n\n")

# DataFrame 생성 방법은 기본적으로 Series 생성 방법과 동일
# 2차원 리스트로 생성
# numpy의 2차원 배열로 생성
# 엑셀의 csv 파일로 생성

# pandas.DataFrame(2차원 리스트, index=[리스트], columns=[리스트])
print("-" * 5, '2차원 리스트로 DataFrame 생성', "-" * 5)

value_list = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

index_list = ['one', 'two', 'three']
columns_list = ['A', 'B', 'C']

df1 = pd.DataFrame(value_list, index=index_list, columns=columns_list)

print("df1 : \n{0}\n{1}".format(df1, type(df1)))


print()
print("-" * 5, '넘파이의 2차원 배열로 DataFrame 생성', "-" * 5)
arr2 = np.array(value_list)
print("arr2 : \n{0}\n{1}".format(arr2, type(arr2)))

df2 = pd.DataFrame(arr2, index=index_list, columns=columns_list)
print("df2 : \n{0}\n{1}".format(df2, type(df2)))

print()
print("-" * 5, '딕셔너리로 DataFrame 생성', "-" * 5)
dic1 = {
    'one':[10,20,30],
    'two':[40,50,60],
    'three':[70,80,90]
}

df3 = pd.DataFrame(dic1)
print("df3 : \n{0}\n{1}".format(df3, type(df3)))


print()
print("-" * 5, 'csv 파일로 DataFrame 생성', "-" * 5)

df4 = pd.read_csv('apt2.csv')
print("df4 : \n{0}\n{1}".format(df4, type(df4)))

# 조회하기
# dataFrame['열이름'] : 해당 열의 데이터를 가져옴
# dataFrame.loc['행이름'] : 지정한 행의 데이터를 가져옴
# dataFrame.iloc[index] : 지정한 행의 데이터를 가져옴, index번호로 동작
print(df2)
print(df2['A'])
print(df2['B'])
print(df4['단지명'].head(10))
print(df2.loc['one'])
print(df2.iloc[2])

# 행 추가하기
# DataFrame.loc['행이름'] = 데이터
print('원본 df2 : \n{0}'.format(df2))
df2.loc['four'] = [100, 90, 80]
print('데이터 추가 후 df2 : \n{0}'.format(df2))

# 열 추가 하기
# 컬럼이 추가 되기 때문에 새로운 DataFrame을 생성해야 함
# DataFrame(원본데이터, columns=[컬럼이 추가된 리스트])
# 새로운 컬럼을 추가하면 해당 컬럼은 데이터가 없음
# DataFrame['컬럼명'] = [리스트]
df2_2 = pd.DataFrame(df2, columns=['A', 'B', 'C', 'D'])
print(df2_2)
print('빈 컬럼에 데이터 추가하기')
df2_2['D'] = [35, 65, 95, 75]
print(df2_2)

# 행, 열 삭제하기
# axis : 0이면 행을 삭제, 1이면 열을 삭제
# drop() 사용 시 원본은 그대로 두고 삭제된 데이터로 만들어진 새로운 DataFrame을 반환함
# drop() 사용 시 inplace = True 옵션을 추가하면 원본의 데이터를 삭제
# DataFrame.drop('행 혹은 열의 이름', axis=0)
print()
print('현재 df2_2 : \n{0}'.format(df2_2))
df2_3 = df2_2.drop('A', axis=1)
print('열 삭제 후 df2_3 : \n{0}'.format(df2_3))
df2_4 = df2_2.drop('one', axis=0)
print('행 삭제 후 df2_4 : \n{0}'.format(df2_4))
df2_2.drop('one', axis=0, inplace=True)
df2_2.drop('A', axis=1, inplace=True)
print('inplace=True로 삭제 후 df2_2 : \n{0}'.format(df2_2))