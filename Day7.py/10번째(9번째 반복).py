# while문을 가지고 만든다.  

numbers =[] # 리스트 (모든 값을 넣는다.)

def print_menu():
    print("----------------- 메뉴 -----------------")
    print("1. 추가, 2. 보여주기, 3. 삭제, 4.종료(999)")

def  input_num():
    return input("값 입력 : ")

def select_numbers():
    num  = int(input('추가할 값 : '))
    numbers.append(num)
def select_see() : 
    for item in numbers:
        print(item)
def del_numbers() : 
    value = int(input("삭제할 값 : "))
    var = 0
    for item in numbers : 
        if value == item :
            del numbers[var]
        var = var + 1 
#  너가 인덱스로 삭제를 할 것인지, 아니면 값을 가지고 삭제를 할 것인지? 그거는 내가 정한다. 
#  인덱스로 삭제할거면 del를 이용하면 된다. 값을 가지고 삭제할거면 remove로 하면 된다. 
# 여기서 인덱스를 이용해서 삭제할거면 변수가 하나가 필요하다. 왜냐하면 인덱스를 담을 수 있는 변수가 없다. 그래서 하나 만들어야한다. 
# 즉, 삭제한다면 del과 remove의 과정은 똑같다. 다만, 새로운 변수가 필요하냐 아니냐의 차이다. 
                   

while True : 
    print_menu() # 메뉴 출력
    select = input_num() # 입력 
    #print(numbers)
    if select == '1' : # 추가
        select_numbers()
    elif select == '2' : # 보여주기
        select_see()
    elif select =='3' : # 삭제
        del_numbers() 
    elif select == '999':
        break
    



