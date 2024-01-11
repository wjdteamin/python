todos = []
# 할일은 할일번호, 할일, 완료여부로 구성
todos.append({"tno" : 1, "title" : '자바공부', "finish" : False})
todos.append({"tno" : 2, "title" : '스프링 공부', "finish" : False})
todos.append({"tno" : 3, "title" : '파이썬 공부', "finish" : False})

print(todos)
# 딕셔너리는 데이터 한 건이다. 또는 행
# 그리고 딕셔너리를 모은게 리스트다.

# 보통 한줄짜고 한줄 실행해본다.

while True:
    print('--------------------할일 관리--------------------')
    print("1. 목록, 2. 추가, 3. 변경, 4. 삭제, 999(종료)")
    select = input('메뉴 선택 : ')
    if select == '1' :
        print('목록')
    elif select == '2':
        print('추가')
    elif select == '3':
        print("변경")
    elif select == '4' :
        print("삭제")
    elif select =='999':
        print('이용해주셔서 감사합니다.')
        break