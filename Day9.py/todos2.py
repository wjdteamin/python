# todo를 만들어보자
# 0. 딕셔너리를 저장할 리스트를 생성한다.
# 0-1. 값을 저장할 딕셔너리를 생성해야한다.
# 1. 일단 반복문을 해야한다
# 2. 메뉴를 출력해야한다. 
# 3. 그리고 원하는 메뉴를 입력받아야한다.
# 4. 메뉴를 변수에 저장하여 찾는다. 
# 5. 함수를 만들어서 실행시킨다. 

todos = []
todos.append({"tno" : 1, "title" : "고기 사기", "finish" : False})
todos.append({"tno" : 2, "title" : "빵 사기", "finish" : False})
todos.append({"tno" : 3, "title" : "라면 사기", "finish" : False})

tno = 4
# 목록 
def print_todos():
     for item in todos :
          print(item)

def  add_todos():
     # 추가할 값을 입력 받는다.
     global tno
     title = input("추가할 title : ")
     todos.append({"tno" : tno, "title" : title, "finish" : False})
     tno = tno +1 # 값을 변경하기 위해서는 global선언해야한다. 

# 타이틀을 수정하겠지?
# i라는 변수를 밖에 선언하고 함수를 사용하면 초기화가 되지 않는다. 이러면 수정 되지 않았는데, 없습니다.라는 문구가 나오지 않는다.
def update_todos():
    i = 0
    update_detail = input("수정할 내용 : ")
    detail = input("수정 내용 : ")
    for item in todos : 
          if update_detail == item["title"]:
               item["title"] = detail
               i = 1
    if i == 0 :
         print("없습니다.")     

def del_todos():
    i = 0
    # 데이터를 가지고 찾는 것이다.
    """
    del_detail = input("삭제할 내용 : ")
    for item in todos:
          if del_detail == item["title"]:
               todos.remove(item)
               i = 1
               print("삭제되었습니다.")
    if i == 0 :
        print("없습니다.")  
    """
    # 인덱스를 가지고 찾는 것 
    del_detail_number = int(input("삭제할 번호: "))
    for item in todos:
          if del_detail_number == item["tno"]:
               todos.remove(item)
               print("삭제되었습니다.")
               i = -1
          i+=1
    if i != -1 :
        print("없습니다.")  




# 무한루프는 while을 가지고 만든다.
while True:
    print("-------------------- 할일 선택-----------------------")
    print("1 : 목록, 2 : 추가, 3 : 변경, 4 : 삭제, 999(종료)")
    numbers = input("메뉴 번호 입력 : ")
    if numbers == '1' :
        print_todos()
    elif numbers == '2' :
        add_todos()
    elif numbers == '3' :
        update_todos()
    elif numbers == '4' :
        del_todos()
    elif numbers == '999':
        print("잘가요")
        break
