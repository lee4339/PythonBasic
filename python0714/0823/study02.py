import csv

print('-' * 5, '게시판의 글을 csv 파일로 만들기', '-' * 5)

data_list_ori = [
    ['글번호', '제목', '글쓴이', '작성일', '조회수', '추천수'],
    ['519304', '시누아타 잎 빤딱 너무 예쁘다', '벌레시러', '20:14', 24, 0],
    ['519303', '쇼크 흙에 들어가도 괜찮음?', 'ㅇㅇ', '20:11', 6, 0],
    ['519302', 'N행시 만들어주는 사이트 [8]', 'ㅇㅇ', '20:03', 87, 3],
    ['519301', '[N행시] 에스쿠엘레토', 'K+', '20:03', 28, 1],
    ['519300', '베란다에서 키우기 좋은 작물 추천좀 [6]', 'ㅇㅇ', '19:56', 45, 0]
]

# csv 파일 쓰기
write_file = open('bbs.csv', 'w', encoding='UTF-8', newline='')

csv_obj_writer = csv.writer(write_file, delimiter=',')
csv_obj_writer.writerows(data_list_ori)

write_file.close()

# csv 파일 읽기
data_list_read = []

read_file = open('bbs.csv', 'r', encoding='UTF-8')

read_data = csv.reader(read_file, delimiter=',')
for item in read_data:
    data_list_read.append(item)

read_file.close()

# csv 파일에서 가져온 데이터 화면 출력
# print(data_list_read)
for item in data_list_read:
    print(item)












