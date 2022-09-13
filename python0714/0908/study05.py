import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('survey.csv')

# 평균 / 합계 구하기
print(df.mean(numeric_only=True))

# 수입의 평균 / 합게
print("수입의 합계 : {0}".format(df.income.sum()))
print("수입의 평균 : {0}".format(df.income.mean()))
print("수입의 중간값 : {0}".format(df.income.median()))

# describe() 함수를 사용하여 요약해서 확인 가능
print(df.describe())

print("수입의 통계 : \n{0}".format(df.income.describe()))

print()
# value_counts() 함수 사용 시 빈도 분석 가능
print(df.sex.value_counts())

# groupby() : 그룹을 나누기
# df.groupby(그룹을 나눌 변수).연산함수
print()
print(df.groupby(df.sex).mean())
print()
print(df.groupby(df.sex).sum())

plt.plot(df.groupby(df.sex).mean())
plt.show()

