# 게시판 dao 작성
board_list = []
bno = 1

# 게시판은 글번호, 제목, 내용, 글쓴이, 조회수로 구성

# save


def save(title: str, content: str, writer: str) -> bool:
    global bno
    board = dict(bno=bno, title=title, writer=writer, content=content, readcnt=0)
    board_list.append(board)
    bno += 1
    # return True -> 검사를 위한 코드?


def findall() -> list:
    return board_list


def delete(bno: int) -> bool:
    for b in board_list:
        if b['bno'] == bno:
            board_list.remove(b)
            return True
    return False
