# 1. 
import datetime as dt

# 2.
board_list = []
bno = 1

# 3.
def list():
    return board_list

# 4. 
def save(title, content, writer):
    global bno
    writeday = dt.datetime.now().date()
    board = dict(bno=bno, title=title, writer=writer, content=content, writeday=writeday, views=0)
    board_list.append(board)
    bno += 1
    return True

# 5.
def read(bno):
    for board in board_list:
        if board['bno'] == bno:
            board['views'] += 1
            return board
    return False

# 6.
def update(bno, title, content):
    for board in board_list:
        if board['bno'] == bno:
            board['title'] = title
            board['content'] = content
            return True

# 7.
def delete(bno):
    for board in board_list:
        if board['bno'] == bno:
            board_list.remove(board)
            return True
    return False
