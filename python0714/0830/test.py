print('-' * 5, 'pyinstaller로 실행파일 만들기', '-' * 5)

print('컴퓨터에 python이 설치되어 있지 않아도 프로그램이 동작함')

# pyinstaller : 시스템에 python이 설치되어 있지 않아도 프로그램을 실행할 수 있도록 만들어주는 모듈
# windows용 실행 파일인 exe 파일을 생성함
# 다운 : pip install pyinstaller
# ==> 터미널에서 +부분에서 command prompt 클릭 후 입력해서 설치
# 사용 : pyinstaller --onefile '파일명.py'
# ==> dist폴더가 생성되고 해당 폴더안에 실행파일이 만들어져 있음