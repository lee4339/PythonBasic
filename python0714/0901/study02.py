from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time



url = 'https://www.coffeebeankorea.com/store/store.asp' # main/main.asp
wd = webdriver.Chrome('chromedriver.exe')

# 가맹점 100개의 정보를 가져옴
stores_info = []

for i in range(1, 10):
    wd.get(url)
    time.sleep(1)

    try:
        wd.execute_script('storePop2({0})'.format(i))
        time.sleep(1)
        html = wd.page_source
        soup = bs(html, 'html.parser')

        store_txt = soup.find('div', {'class' : 'popup_inner'}).find('div', {'class':'store_txt'})

        store_name = store_txt.find('h2').text.strip()
        store_info_list = store_txt.find_all('td')
        store_address = store_info_list[2].text.strip()
        store_tel = store_info_list[3].text.strip()

        stores_info.append({'name': store_name, 'address': store_address, 'tel': store_tel})
    except:
        continue

for item in stores_info:
    print('이름 : {0}\n주소 : {1}\n전화번호 : {2}\n'.format(item['name'], item['address'], item['tel']))
    print('-' * 10)

print(stores_info)