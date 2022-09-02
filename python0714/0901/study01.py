# 셀레니움 : 파이썬에서 웹 크롤링을 하기 위한 라이브러리 중 하나로 동적 크롤링을 할 수 있도록 도와주는 라이브러리
# 셀레니움은 뷰티풀수프와 다르게 웹 드라이버라고 하는 웹 브라우저 원격 제어기를 이용하여 실제 웹 브라우저를 통해서 웹의 정보를 크롤링 함

from selenium import webdriver
import time

print('-' * 5, '셀레니움 사용하기', '-' * 5)

# webdriver.Chrome(웹드라이버 경로) : 웹 드라이버를 사용하여 실제 웹 브라우저를 동작 시킴
# Chrome, Firefox, Edge, Safari 각각의 웹 드라이버를 다운 받아서 사용해야 함
# get(웹주소) : 지정한 웹 사이트로 접속
# quit(), close() : 웹 사이트 종료
# find_element_by_id(id) : html 태그의 id 속성을 가지고 있는 html 태그를 가져옴
# find_elements_by_name(태그이름) : html 태그 이름을 기준으로 html 태그를 모두 가져옴
# find_elements_by_class_name (class명) : html 태그의 class 속성을 기준으로 html 태그를 모두 가져옴
# find_elements_by_css_selector("css 선택자") : 지정한 css 선택자를 사용하여 html 태그를 모두 가져옴, 리스트로 가져옴
# send_keys(문자열) : 문자열을 입력
# click() : 지정한 태그를 마우스 클릭
# execute_script(자바스크립트) : 자바스크립트를 실행
# page_source : 지정한 태그의 html 코드를 가져옴

wd = webdriver.Chrome('chromedriver.exe')

wd.get('https://www.naver.com')
time.sleep(3)

wd.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
time.sleep(3)
wd.find
user_id = wd.find_element_by_id('id')
user_pw = wd.find_element_by_id('pw')

user_id.send_keys('asdf')
user_pw.send_keys('asdf1234')

time.sleep(3)

wd.find_element_by_id('log.login').click()
# wd.quit()




