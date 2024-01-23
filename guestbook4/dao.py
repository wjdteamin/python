# 웹프로그래밍을 이렇게 만들자 : MVC
# Model : 데이터 -> model의 조작을 담당하는 파일(DAO)
# 데이터에 접근하는 객체이다. 즉 DB를 사용해서 CRUD를 수행하는 객체
# View :화면
# Controller : 모델과 뷰를 연결한다.
import datetime as d

# 모델
guestbook = []

gb = dict(gno=1, nickname="관리자", content="욕설, 비방은 경고없이 삭제합니다.", writeday="2024-01-23")
guestbook.append(gb)
# 일련번호는 보통 key로 사용된다.
# 문자열은 오타 위험이 있어서 보통 key는 숫자
gno = 2

# crd


def save(nickname: str, content: str) -> bool:
    global gno
    writeday = d.datetime.now().date()
    gb = dict(gno=gno, nickname=nickname, content=content, writeday=writeday)
    guestbook.append(gb)
    gno += 1
    return True


def findall():
    return guestbook

# def findone(): -> 하나 읽기


# return : 함수를 종룔하고 결과 값을 남겨라
# break는 반복문을 빠져나간다. 그래서 밑으로 내려가기 때문에 return을 사용하는 것이 맞다.
def delete(gno: int) -> bool:
    for gb in guestbook:
        if gb['gno'] == gno:
            guestbook.remove(gb)
            return True
    return False
