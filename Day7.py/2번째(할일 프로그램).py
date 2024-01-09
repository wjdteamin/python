todos = [
    {"tno" : 1, "title" : "자바공부", "finish" : False},
    {"tno" : 3, "title" : "파이썬공부", "finish" : False}
]
# 계산하면 돈이다. 
# 클라우드를 이용하기 때문에 무슨 짓을 하면 돈이 빠져나간다. 

#tno = 4 
# Crate (생성)
"""
title = input('할일 입력 : ')
todo = {"tno" : tno, "title" : title, "finish" : False}
todos.append(todo)
tno += 1
#print(todos)
#print(tno)

# Read : todos 출력
r = 0
for x in todos : 
    print(todos[r])
    r+=1
"""
for x in todos : 
    print(x)

# Update (번호로 찾아서 업데이트) -> tno로 찾아 finish를 toggle(스위치를 켰다, 껐다를 해준다. )
# 못 찾으면 아무것도 하지 않는다.
#a = 0
"""
input_tno = int(input("변경할 할일 번호"))
# for in, if를 가지고 반복하고 값을 찾는다.
for todo in todos :
    if todo['tno'] == input_tno:
        todo['finish'] = not todo['finish']
 #       a=1
        break
    # else라는 코드를 추가하면 하나씩 확인하기 때문에 else도 todos 개수만큼 반복된다. 
print(todos)
if a == 0 :
    print('없습니다.')
"""

    # 그럼 없습니다를 나타내고 싶으면 어떻게하지? 
"""
for todo in todos : 
    if todo['finish'] != True:
        print("없습니다.")
"""

# 기획자를 해야한다. 그게 이 나라에서 살아남는 법이다. 기획을 잘해야한다.


# 삭제 : 원하는 값을 입력해서 그걸 찾는다. 그리고 그걸 찾는다.
# 삭제 : 지운다.
# 원하는 tno에 해당하는 todo를 todos에서 찾는다. 

input_tno = int(input("삭제할 할일번호 입력 : "))
for todo in todos : 
# todos(리스트)에서 값을 하나씩 꺼낸다. 그리고나서 그 값을 todo에 담는다. 
    if todo['tno'] == input_tno : 
# todo는 리스트에서 얻은 딕셔너리 값이다. 그걸 가지고 내가 입력한 숫자와 대조해본다. 
        # del list[인덱스]
        # list.remove(딕셔너리)
        todos.remove(todo)
        break
print(todos)

# 내가 변경할 수 있는 값과 없는 값을 구분해야한다. 