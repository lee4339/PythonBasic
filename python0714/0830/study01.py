#https://www.crummy.com/software/BeautifulSoup/bs4/doc/#

# 다음 뉴스 홈의 뉴스 리스트 가져오기
# 1. 뉴스의 타이틀 가져오기
# 2. 뉴스의 주소 가져오기
# 3. 해당 뉴스 페이지의 첫번째 문자

# 순서
# 1. 접속 사이트 주소 입력
# 2. urlopen()으로 지정한 사이트 접속
# 3. 뷰티풀수프로 가져온 데이터 html로 파싱
# 4. find_all(), find()로 원하는 데이터 가져오기(부모 데이터)
# 5. 반복문을 사용하여 실제 데이터 부분을 find(), find_all()로 가져오기
# 6. 제목, 주소, 내용을 파일에 저장

import urllib.request as ur
from bs4 import BeautifulSoup as bs

url = 'https://news.daum.net/'

web_data = ur.urlopen(url)
html = bs(web_data.read(), 'html.parser')

item_issue_list = html.find_all('div', {'class':'item_issue'})

news_list = []
for items in item_issue_list:
    # strong = items.find('strong')
    # a = strong.find('a')
    a = items.find('strong').find('a')
    title = a.text.strip()
    link = a.get('href')

# 찾은 url 주소를 가지고 urlopen() 함수를 이용해서 다시 웹사이트 접속
# 뷰티풀 수프로 다시 html 파싱
#     sub_web_data = ur.urlopen(link)
#     sub_html = bs(sub_web_data.read(), 'html.parser')

# sub_url = 'https://v.daum.net/v/20220830201918357'
    sub_web_data = ur.urlopen(link)
    sub_html = bs(sub_web_data.read(), 'html.parser')

    article_view = sub_html.find('div', {'class' : 'article_view'})
    p_list = article_view.find_all('p', {'dmcf-ptype' : 'general'})
    news = p_list[1].text.strip()

    news_item = {'title': title, 'news': news, 'link': link}
    news_list.append(news_item)
    # print('제목 : {0}\n내용: {1}\n링크 : {2}\n'.format(title, news, link),'-' * 20, '\n')

f = open('daum_news_issue.txt', 'w', encoding='utf-8')
for item in news_list:
    new_str = '제목: {0}\n내용: {1}\n링크: {2}\n\n'.format(item['title'],item['news'], item['link'])
    f.write(new_str)
f.close()
