import  googletrans
# from googletrans import Translator

print("-" * 5, "구글 번역기 라이브러리 사용하기", "-" * 5)

# googletrans 모듈은 아나콘다에 포함되어 있지 않음
# pip을 사용하여 따로 설치가 필요함

# 설치 방법 :
# 1. pycharm의 터미널 버튼 클릭
# 2. v 버튼을 클릭하여 command Prompt 실행
# 3. pip install googletrans==4.0.0-rc1 입력
# 3.1 그냥 pip install googletrans로 설치 시 모듈을 실행하면 오류발생

# googletrans 사용법
# import googletrans
# from googletrans import Translator

# translator = Translator()
# print(translator.translate('안녕하세요', dest='en'))

# googletrans는 구글 번역 ajaxApi를 구현한 클래스
# 2개의 함수를 사용함

# translate('번역할 문자열', dest='타켓언어', src='원본언어')
# 입력한 문자열을 지정한 언어로 번역하는 함수
# src는 auto를 사용하거나 생략가능

# detect('확인할 문자열')
# 입력한 언어를 자동으로 감지하여 어떠한 언어인지 알려주는 함수

translator = googletrans.Translator()

trans_txt = translator.translate('안녕하세요')
print("원본 언어 : {0}, {1}\n번역 언어 : {2}, {3}".format(
    trans_txt.src, trans_txt.origin, trans_txt.dest, trans_txt.text))

trans_txt = translator.translate('hello', dest='ko')
print("원본 언어 : {0}, {1}\n번역 언어 : {2}, {3}".format(
    trans_txt.src, trans_txt.origin, trans_txt.dest, trans_txt.text))


str = "Chandler: Oh, uh, that would be mine. See, I wrote a note to myself, and then I realised I didn't need it, so I balled it up and... (sees that Monica is glaring at him) ...now I wish I was dead."

trans_txt = translator.translate(str, dest="ko")
print(trans_txt)