import usecsv

print('-' * 5, 'usecsv 모듈로 csv 파일 사용하기', '-' * 5)

data_list = usecsv.open_csv('bbs.csv')

print(data_list)

usecsv.write_csv('bbs_copy.csv', data_list)


