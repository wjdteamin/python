# board_list = []
# board_list.append(dict(bno=1, title="1번", nickname="하우스", views=0, content="집에 가고싶어요"))
# board_list.append(dict(bno=2, title="2번", nickname="이우스", views=0, content="집에 가고파"))
# board_list.append(dict(bno=3, title="3번", nickname="리우스", views=0, content="집에 그냥"))
# board_list.append(dict(bno=4, title="4번", nickname="한우스", views=0, content="집에 원해?"))

# bno = 5


# def findall():
#     return board_list

# # 작업을 2개 - 조회수 증가


# def findone(bno):
#     for b in board_list:
#         if b['bno'] == bno:
#             # 증가시키는 것이다.
#             b['views'] = b['views']+1
#             return b
#     return False


# def save(title: str, nickname: str, content: str) -> bool:
#     global bno
#     bol = dict(bno=bno, title=title, nickname=nickname, views=0, content=content)
#     board_list.append(bol)
#     bno += bno


# def delete(bno: int) -> bno:
#     for b in board_list:
#         if b['bno'] == bno:
#             board_list.remove(b)


# erd 설계 -> ???

# 데이터 : model
# 모델을 다루는 클래스 : DAO -> Data Access Object라고 한다. (DAO, 다오)

# 상품 dao
# 검색 : 전체출력, 상품하나의 상세 정보, 기능 별 검색, 인기 순 검색(top 검색), 가격 높은 순, 낮은 순 검색, 구매 많은 순, 적은 순
# 분야 별 검색, 세일에 관한 검색,  내가 자주 구매했던 상품, 구매할만한 상품 -> 전부 다 read에 관한 것이다 .

# 코딩을 하는 사람보다는 기획하는 사람이 더욱 더 중요하다.

# 추가(save), 전체출력(findall), 하나출력(findone), 변경(update), 삭제(delete)

# 글 : 글번호, 제목, 내용, 닉네임, 조회수


board_list = []
bno = 1


def findall():
    return board_list


def findone(bno):
    for board in board_list:
        if board['bno'] == bno:
            board['views'] += 1
            return board
    return False


def save(title, content, nickname):
    global bno
    bol = dict(bno=bno, title=title, content=content, nickname=nickname, views=0)
    board_list.append(bol)
    bno += 1
    return True


def update(bno, title, content):
     for board in board_list:
         if board['bno'] == bno:
             board['title'] = title
             board['content'] = content
             return True


def delete(bno):
    for board in board_list:
        if board['bno'] == bno:
            board_list.remove(board)
            return True
    return False
