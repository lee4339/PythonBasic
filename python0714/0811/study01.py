print("-" * 5, "예외 발생시키기", "-" * 5)


#클래스 = 함수, 변수 생성하기 위한 틀(설계도)
class Bird:
    def fly(self):
        print("날아갑니다.")
        #raise NotImplementedError


class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()


print("-" * 5, "사용자 예외 생성하기","-"* 5)

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명"

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

say_nick("파이썬")

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print("별명 입력 중 에러가 발생했습니다.")
    print(e)