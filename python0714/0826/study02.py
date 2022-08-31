from bs4 import BeautifulSoup as bs
import urllib.request as ur

# 1. 접속할 사이트 주소 입력
# 2. urlopen()로 지정한 사이트 접속 및 데이터 가져오기
# 3. 뷰티풀수프로 가져온 데이터 html 데이터로 변경하기(파싱)
# 4. 변경된 데이터에서 find_all()을 사용하여 원하는 부분의 데이터만 전부 가져와서 리스트에 저장
# 5. find()를 사용하여 원하는 부분의 데이터를 상세하게 검색하여 가져오기

# 실제 접속할 주소
url = 'https://news.daum.net/'

# 웹 서버에 접속하여 데이터를 전달
html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')

# 원하는 데이터가 있는 최상위 부모 태그를 가져옴
full_data = soup.find('ul', {'class' : 'list_newsissue'})
# data_list = full_data.find_all('div', {'class' : 'item_issue'})

strong_list = full_data.find_all('strong')

file_data_list = []

for item in strong_list:
    # 태그.get('속성명) : 해당 태그의 속성값을 가져옴
    a = item.find('a')
    text = a.text.strip()
    link = a.get('href')
    print('\n-', '제목 : {0}\n주소 : {1}'.format(text, link), '\n')
    data = '-제목 : {0}\n주소 : {1}'.format(text, link) + '\n\n'
    file_data_list.append(data)

f = open('daumnew.txt', 'w', encoding='utf-8')
f.writelines(file_data_list)
f.close()



