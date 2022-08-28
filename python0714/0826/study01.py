import urllib.request as ur
# import bs4
from bs4 import BeautifulSoup as bs

# as : 모듈의 이름이 길 경우 별명을 사용하여 짧은 이름을 사용

# 웹 크롤링 : 웹 사이트에 웹 브라우저가 아닌 파이썬 라이브러리를 통해서 접근하여 사용자가 원하는 정보를 가져오는 기술
# beautifulsoup4 : 웹 크롤링을 쉽게 하기 위해서 사용하는 라이브러리
# requests : 웹 서버에 웹 브라우저 없이 데이터 요청을 할 수 있도록 해주는 라이브러리

print('-' * 5, '웹 크롤링 사용하기', '-' * 5)
# 1. 접속할 사이트 주소 입력
# 2. urlopen()로 지정한 사이트 접속 및 데이터 가져오기
# 3. 뷰티풀수프로 가져온 데이터 html 데이터로 변경하기(파싱)
# 4. 변경된 데이터에서 find_all()을 사용하여 원하는 부분의 데이터만 전부 가져와서 리스트에 저장
# 5. find()를 사용하여 원하는 부분의 데이터를 상세하게 검색하여 가져오기


# 접속할 사이트 주소 입력
url = 'https://quotes.toscrape.com/'

# 지정한 사이트 주소로 접속 및 데이터 가져오기
html = ur.urlopen(url)
print(html)

print()
# 웹에서 받아온 데이터를 뷰티풀수프 모듈을 통해서 html 방식으로 읽어들임
# 데이터를 읽는 방식은 html, xml, text
# 현재 페이지의 모든 html 태그 내용을 다 가져옴

# 웹에서 가져온 데이터를 html 방식으로 변경
soup = bs(html.read(), 'html.parser')
# print(soup)
# find_all(태그이름) : html의 내용 중 지정한 태그를 모두 가져와서 리스트에 저장
# find_all로 가져온 데이터에 .text 를 사용 시 해당 태그의 글자만 가져옴
# find_all(태그이름, {속성명: 속성값}) : 지정한 태그명에서 지정한 속성값을 가지고 있는 태그만 검색하여 리스트에 저장
# find(태그이름) : html의 내용 중 지정한 태그를 검색하여 가장 먼저 검색된 태그만 가져옴
span_list = soup.find_all('span')
# print(span)
print(span_list[0])
print(span_list[0].text)

print()
# 태그 이름과 지정한 속성값을 가지고 있는 태그만 가져옴
div_list = soup.find_all('div', {'class' : 'quote'})
print(div_list)
print(len(div_list))

print()
text_list = []
# 리스트에 저장도딘 내용을 반복문 통해서 전체 검색
for items in div_list:
    # 실제 필요한 부분에 대한 정보를 가져오기 위해서 find() 함수를 사용
    text = items.find('span', {'class' : 'text'}).text
    author = items.find('small', {'class' : 'author'}).text
    print('명언 : {0}\n- {1} -'.format(text, author))
    text_list.append(text + '-' + author + '-\n')

f = open('text.txt', 'w', encoding='UTF-8')
f.writelines(text_list)
f.close()

