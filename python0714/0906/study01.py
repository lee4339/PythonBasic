import numpy as np

print('-' * 5, 'numpy 사용하기', '-' * 5)


# numpy : 배열과 행렬을 쉽게 사용하도록 도와주는 패키지
# shape() : 배열의 크기를 튜플로 반환
# dtype : 배열을 구성하는 요소의 타입의 반환
# int(32, 64) : 부호가 있는 정수
# uint(32, 64) : 부호가 없는 정수
# float(32, 64) : 실수
# complex : 복소수
# bool : 논리형 (boolean), 참 혹은 거짓을 가지는 자료형
# string : 문자열
# object : 파이썬 오브젝트
# unicode : 유니코드
# astype(타입) : 지정한 타입으로 요소의 타입을 변경
# numpy.arange(시작, 종료) : range()와 같이 지정한 숫자에서 지정한 숫자까지의 배열을 생성하는 함수
# numpy.zeros(행, 열) : 지정한 크기의 배열을 생성하는데 요소를 모두 0으로 설정
# numpy.ones(행, 열) : 지정한 크기의 배열을 생성 시 요소를 모두 1로 설정
# numpy.transpose(행, 열) : 지정한 크기의 배열로 배치

# 2 X 2 배열 생성
a = np.array([
    [2, 3],
    [5, 6]
])

print(a)
print(type(a))

# 2차원 리스트 생성
b = [
    [2, 3],
    [5, 2]
]

print(b)
print(type(b))

# 넘파이의 배열은 파이썬의 리스트와 비슷하게 사용이 가능함

d = np.array([
    [1, 2, 3, 4, 5],
    [2, 4, 5, 6, 7],
    [5, 6, 7, 8, 9]
])
print(d)
print('d[0][0] : {0}'.format(d[0][0]))
print('d[0][1] : {0}'.format(d[0][1]))
print('d[0][-1] : {0}'.format(d[0][-1]))
print('d[1][2] : {0}'.format(d[1][2]))   # 리스트에서 사용하는 indexing 방식
print('d[1, 2] : {0}'.format(d[1, 2]))   # 위에와 같은 결과가 나온다 // 넘파이에서 사용가능한 방식
print('d[1:, 3:] : {0}'.format(d[1:,3:]))
# 인덱싱은 지원하지만 슬라이싱으로는 지원되지 않음
print('d[1:][3:] : {0}'.format(d[1: ][3:]))  # 지원안함

print()
e = np.array([2, 3, 4, 5, 6])
print(e)
print('배열 e의 크기 : {0}'.format(e.shape))

f = np.array([
    [1, 2, 3, 4],
    [3, 4, 5, 6]
])

print(f)
print('배열 f의 크기 : {0}'.format(f.shape))
print(f.dtype)

print()

data = np.arange(1, 5)
print('생성된 데이터 : {0}'.format(data))
print('data의 타입 : {0}'.format(type(data)))
print('배열 data가 가지고 있는 요소의 타입 : {0}'.format(data.dtype))
data = data.astype('float64')
print('astype를 사용 후 배열 data가 가지고 있는 요소의 타입 : {0}'.format(data.dtype))
print('astype 사용 후 배열 data : {0}'.format(data))
data = data.astype('int32')
print('astype를 사용 후 배열 data가 가지고 있는 요소의 타입 : {0}'.format(data.dtype))
print('astype 사용 후 배열 data : {0}'.format(data))

print()

g = np.zeros((2, 5))
print(g)

print()

h = np.ones((2, 5))
print(h)

print()

i = np.transpose(h)
print(i)


print('-' * 5, 'numpy 배열 연산', '-' * 5)

arr1 = np.array([
    [2, 3, 4],
    [6, 7, 8]
])

arr2 = np.array([
    [12, 23, 14],
    [36, 47, 58]
])

arr3 = np.array([100, 200, 300])

print('원본 배열 arr1 : \n{0}'.format(arr1))
print('원본 배열 arr2 : \n{0}'.format(arr2))
print('원본 배열 arr3 : \n{0}'.format(arr3))

# 배열의 사칙연산 시 두 배열의 행과 열이 동일하면 각각 같은 자리의 수끼리 연산을 진행함
print('arr1 + arr2 : \n{0}'.format(arr1 + arr2))
print('arr1 * arr2 : \n{0}'.format(arr1 * arr2))
print('arr1 / arr2 : \n{0}'.format(arr1 / arr2))

print()

# 크기가 다를 경우 모든 행에 덧셈이 진행됨
print('arr1 + arr3 : \n{0}'.format(arr1 + arr3))

# arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# # 행과 열의 크기가 모두 다를 경우 오류가 발생함
# print('arr1 + arr4 : \n{0}'.format(arr1 + arr4))

arr5 = np.array([
    [9],
    [3]
])

# 행과 열의 크기를 만족하면 덧셈이 가능
print('arr1 + arr5 : \n{0}'.format(arr1 + arr5))

print()

print('-' * 5, 'numpy의 배열과 파이썬의 리스트 차이', '-' * 5)

j_array = np.array([
    [1,2 ,3 ,4, 5],
    [2, 4, 5, 6, 7],
    [5,7, 8, 9, 9]
])

j_list = [
    [1,2 ,3 ,4, 5],
    [2, 4, 5, 6, 7],
    [5,7, 8, 9, 9]
]

print('j_array : \n{0}'.format(j_array))
print('k_list : \n{0}'.format(j_list))

# 리스트는 슬라이싱 기법으로 데이터를 가져오는 것만 가능
# 리스트는 슬라이싱 기법으로 데이터를 저장하는 것은 지원하지 않음
# print(j_list[:2])
# j_list[:2] = 0

# 배열은 슬라이싱 기법으로 데이터를 가져오거나 저장하는 것이 가능함
print(j_array[:2])
j_array[:2] = 0
print('j_array[:2] = 0 : \n{0}'.format(j_array[:2]))

