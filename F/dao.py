board_list = []
board_list.append(dict(bno=1, title="1번", nickname="하우스", views=0, content="집에 가고싶어요"))
board_list.append(dict(bno=2, title="2번", nickname="이우스", views=0, content="집에 가고파"))
board_list.append(dict(bno=3, title="3번", nickname="리우스", views=0, content="집에 그냥"))
board_list.append(dict(bno=4, title="4번", nickname="한우스", views=0, content="집에 원해?"))

bno = 5


def findall():
    return board_list

# 작업을 2개 - 조회수 증가


def findone(bno):
    for b in board_list:
        if b['bno'] == bno:
            # 증가시키는 것이다.
            b['views'] = b['views']+1
            return b
    return False


def save(title: str, nickname: str, content: str) -> bool:
    global bno
    bol = dict(bno=bno, title=title, nickname=nickname, views=0, content=content)
    board_list.append(bol)
    bno += bno


def delete(bno: int) -> bno:
    for b in board_list:
        if b['bno'] == bno:
            board_list.remove(b)
