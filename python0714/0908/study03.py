import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


data_set = np.random.rand(10, 3)
df = pd.DataFrame(data_set, columns=['A', 'B', 'C'])
print("df : {0}\n{1}".format(type(df), df))

# plt.plot(df)
# plt.show()

font_list = [font.name for font in fm.fontManager.ttflist] # 가지고 있는 모든 폰트
print(font_list)

# plot(데이터) : 지정한 데이터를 기반으로 라인 플롯을 생성하는 함수
# show() : 생성된 plot을 화면에 출력하는 함수
# title(제목) : 생성된 plot의 제목을 설정
# xlabel(라벨제목) : x축의 제목 설정 
# ylabel(라벨제목) : y축의 제목 설정
# legend([리스트]) : 범례 설정

# 그래프 종류 변경
plt.rcParams['font.family'] = 'New Gulim'
plt.title('제목 설정')
plt.plot([1, 2, 3, 4], [2, 4, 8, 6])
plt.plot([1.5, 2.5, 3.5, 4.5], [3, 5, 9, 7])
plt.xlabel('시간')
plt.ylabel('점수')
plt.legend(['A 학생', 'B 학생'])
plt.show()


