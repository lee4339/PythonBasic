import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("-" * 5, '데이터 분석 라이브러리 사용하기', "-" * 5)

# NumPy: 데이터 분석의 기본 기능 제공, 벡터, 행렬 연산과 관련된 기능을 제공
# Pandas: Series, DataFrame 등의 자료 구조를 활용한 데이터 분석에 우수한 성능, 대량의 데이터를 처리 가능
# Matplotlib: 데이터의 시각화, 그래프화 작성

# 난수 생성
data = np.random.rand(50)
print(type(data))
print(data)

#
seri = pd.Series(data)
print(type(seri))
print(seri)

# plt.style.use('ggplot')
# plt.plot(seri)
# plt.show()

data_set = np.random.rand(10, 3)
print(data_set)
print(type(data_set))
print(data_set.shape)

df = pd.DataFrame(data_set)
print(df)
print(type(df))