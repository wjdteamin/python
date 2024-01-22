import datetime as d
guestbook = []
gb1 = dict(gno=1, name="본드", content="첫번째 내용", writeday="20204-01-22")

guestbook.append(gb1)


def list_information():
    return guestbook


gno = 2


def guestbook_save(name, content):
    global gno
    writeday = d.datetime.now().date()
    gb = dict(gno=gno, name=name, content=content, writeday=writeday)
    guestbook.append(gb)
    gno += 1


def guestbook_delete(gno):
    for item in guestbook:
        if gno == item['gno']:
            guestbook.remove(item)
            break


def guestbook_update(gno: int, content: str):
    for item in guestbook:
        if gno == item['gno']:
            item['content'] = content

# 파이썬은 굳이 값을 다시 저장하지 않아도 된다. 주소를 지정하는 것이다. 
# [1,2,3,4,5] -> 값을 꺼내는 것이 아니라 주소를 지정해주는 것이다.

# C -> 저장
# R
# U
# D

# U,D는 일단 찾는거부터 한다
