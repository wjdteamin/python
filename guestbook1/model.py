import datetime as d
# 데이터 : model
guestbook = list()
gno = 3
gb1 = {"gno": 1, "content": "첫번째 방명록", "writeday": "2024-01-22"}
# 파이썬에서 타입은 모두 클래스
# 클래스 이름으로 객체를 생성할 수 있으며 함수처럼 사용
# 따옴표를 사용하기 귀찮기 때문에 앞에 타입을 적어서 따옴표를 쓰지 않고 사용하기 위해서

gb2 = dict(gno=2, content="두번째 방명록", writeday="2024-01-22")


guestbook.append(gb1)
guestbook.append(gb2)


#  리스트 전부 출력 - 스프링은 모델 함수 이름이 정해져있다. 땡겨서 사용
def findall():
    return guestbook

# def delete(tno):
#     for numbers in guestbook:
#         if tno == numbers['tno']:
#             guestbook.remove(numbers)
#     return guestbook


def content_append(content: str):
    global gno
    writeday = d.datetime.now().date()
    gb = dict(gno=gno, content=content, writeday=writeday)
    guestbook.append(gb)
    gno += 1


def hap(val1: int, val2: int) -> int:
    return val1 + val2


# hap(10, 20)
# val1에 10, val2에 20이 들어가야만 한다.
# why? 지금은 인자가 적어서 그렇지만, 인자가 많아지면? 많아지면 실수가 생길 수 있다. 그래서 함수를 호출할 때, 인자 이름을 붙여준다.
hap(val2=20, val1=10)


# 간단 요약
"""
데이터 -> 모델
화면 출력 -> 뷰 

뷰와 모델은 따로 만들어야 재사용하기도 편하고, 읽기도 편하다. 
그런데 뷰와 모델은 서로를 모른다. 그래서 컨트롤를 이용해서 서로를 연결하는 것이다 .


gb1 = {"gno": 1, "content": "첫번째 방명록", "writeday": "2024-01-22"} 와 gb2 = dict(gno=2, content="두번째 방명록", writeday="2024-01-22")의 
차이점은 문자열을 여부정도?


view와 모델을 연결 -> 스프링이나 플라스크의 역할 -> controller
"""
