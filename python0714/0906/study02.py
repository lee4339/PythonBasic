import  usecsv
import  numpy as np

print('-' * 5, 'numpy 사용하기', '-' * 5)

file = usecsv.switch(usecsv.open_csv('quest.csv'))

print('원본데이터 : {0}'.format(file))

quest = np.array(file)
print('배열 데이터 : \n{0}'.format(quest))

# 배열의 데이터를 가지고 와서 5보다 큰 데이터를 확인
print('5보다 큰 데이터 : {0}'.format(quest[quest>5]))

# 배열의 데이터 중 5볻 큰 숫자를 모두 5로 변경
quest[quest>5] = 5
print('변경 후 배열 데이터 : \n{0}'.format(quest))
print('5보다 큰 데이터 : {0}'.format(quest[quest>5]))

usecsv.write_csv('result.csv', quest)