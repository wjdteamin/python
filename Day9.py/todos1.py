todos = []

# 할일은 할일번호, 할일, 완료여부로 구성
todos.append({"tno" : 1, "title" : '자바공부', "finish" : False})
todos.append({"tno" : 2, "title" : '스프링 공부', "finish" : False})
todos.append({"tno" : 3, "title" : '파이썬 공부', "finish" : False})

#print(todos)
# 딕셔너리는 데이터 한 건이다. 또는 행
# 그리고 딕셔너리를 모은게 리스트다.

# 보통 한줄짜고 한줄 실행해본다.

# 변수를 밖에다 선언하면 에러가 난다. 
tno = 4
# def는 함수를 만드는 예약어
def print_todos():
    for item in todos :
        print(item)

def add_todo():
    # 함수 밖에 있는 변수를 변경하려면 global 변수 이름을 작성해야한다. 
    # 단, 읽는 것은 상관없다. 
    global tno
    title = input('할일 입력 : ')
    todos.append({"tno" : tno, "title" : title, "finish" : False})
    tno = tno +1    
# 계속 누적이 된다.

def toggle_finish():
    pass

def delete_todo():
    pass


while True:
    print('--------------------할일 관리--------------------')
    print("1. 목록, 2. 추가, 3. 변경, 4. 삭제, 999(종료)")
    select = input('메뉴 선택 : ')
    if select == '1' :
        print_todos()            #호출
    elif select == '2':
        add_todo()
    elif select == '3':
        toggle_finish()
    elif select == '4' :
        delete_todo()
    elif select =='999':
        print('이용해주셔서 감사합니다.')
        break

    # 함수를 사용하는 이유? 1. 자사용. 2.코드 파악하기가 쉬워진다. 등이 있다.