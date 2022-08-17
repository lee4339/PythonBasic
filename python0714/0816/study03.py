from googletrans import Translator

trans = Translator()

f = open('would.txt', 'r', encoding='UTF-8')
list_text = f.readlines()
f.close()

# 번역
trans_text = ""

for text in list_text:
    if '\n' == text:
        pass
    else:
        trans_obj = trans_dest_text = trans.translate(text, dest="ko")
        trans_text = trans_text + trans_obj.text + "\n"

print("번역 완료\n")
    
# 번역된 문자열을 파일에 저장
f = open('would_ko.txt', 'w', encoding='UTF-8')
f.write(trans_text)
f.close()

print("파일 저장 완료")

# 문제 1) googletrans 모듈을 사용하여 기존에 생성한 take.txt 파일을 읽어서 한글로 번역한 후 take_ko.txt 파일로 저장하는 프로그램을 작성하세요

# 문제 2) rachel.txt 파일을 열고 한글로 번역한 후 rachel_ko.txt 파일로 저장하는 프로그램을 작성하세요.

print()
print("-" * 5, "문제 1번", "-" * 5)
f = open('take.txt', 'r', encoding='UTF-8')
list_text = f.readlines()
f.close()

trans_text = ""
for text in list_text:
    if '\n' == text:
        pass
    else:
        trans_obj = trans_dest_text = trans.translate(text, dest='ko')
        trans_text = trans_text + trans_obj.text + '\n'

f = open('take_ko.txt', 'w', encoding='UTF-8')
f.write(trans_text)
f.close()
print("저장 완료")


print()
print("-" * 5, "문제 2번", "-" * 5)
f = open('rachel.txt', 'r', encoding='UTF-8')
list_text = f.readlines()
f.close()

trans_text = ""
for text in list_text:
    if '\n' == text:
        pass
    else:
        trans_obj = trans_dest_text = trans.translate(text, dest='ko')
        trans_text = trans_text + trans_obj.text + '\n'

f = open('rachel_ko.txt', 'w', encoding='UTF-8')
f.write(trans_text)
f.close()
print("저장 완료")
