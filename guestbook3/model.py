import datetime as d
guestbook = []
gb1 = dict(gno=1, name="본드", content="첫번째 내용", writeday="20204-01-22")
guestbook.append(gb1)
gno = 2


def list_information():
    return guestbook


def write_append(name, content):
    writeday = d.datetime.now().date()
    addes = dict(gno=gno, name=name, content=content, writeday=writeday)
    guestbook.append(addes)


def delete_guestbook(gno):
    for item in guestbook:
        if item['gno'] == gno:
            guestbook.remove(item)
            break


def guestbook_update(gno, content):
    for item in guestbook:
        if item['gno'] == gno:
            item['content'] = content
            break
