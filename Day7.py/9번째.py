# 숫자 리스트 - 추가, 목록, 합계, 변경, 삭제. 함수버전

numbers =[1,3,5]

def print_menu() :
    print('--------------- 숫자 CRUD ----------------------')
    print('1 : 추가, 2 : 목록, 3 : 삭제, 999 : 종료')
def input_select():
    return input("메뉴 선택 : ")
# 값을 함수에서 가지고 있는게 아니라 return으로 돌려보내야한다.

def add_value() : 
    value = int(input('값 입력'))
    numbers.append(value)

def list_numbers() :
    for num in numbers: 
        print(num, end=" ")
        # 줄바꿈대신에 공백을 찍어라
    print()

def delete_numbers() : 
    value = int(input("삭제할 값 입력 : "))
    index = 0 
    for num in numbers : 
        if num == value : 
            del numbers[index]
        index = index + 1
        
while True : 
    print_menu()
    select = input_select()
    if select =='1':
        add_value()
    elif select == '2':
        list_numbers()
    elif select == '3':

        delete_numbers()
    elif select == '999' :
       break