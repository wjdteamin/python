"""
    1. 값추가 : input('숫자 입력 : ')
    2. 리스트 출력 : 
    999. 종료 : 감사합니다. -> 
"""

# 5일만에 드디어 프로그램을 만들었어요! 
리스트 = [] # 저장할 곳


while True : 
    print("1. 값추가")
    #print("2. 리스트 출력")
    #print("3. 리스트 합 출력")
    #print("999. 종료")
    select = input("번호 선택 : ")
    if select == '1':
        num = int(input("숫자 입력 : "))
        리스트.append(num)
    elif select =='2' : 
        print(리스트)
    elif select == '3' :
        
        # 리스트=sum(리스트) 이렇게 하면 원본 데이터를 훼손하게 된다. 그렇기 때문에 이런식으로 만들려면 변수를 따로 만들어야한다. 
        # 음.........

        print(리스트)
    elif select == '999' : 
        print("감사합니다.")
        break
    else :
        print("다시 입력해주세요")

# 일단 리스트에 넣으면 ??? 원리를 모르겠다. 생각해봐야지











""""
리스트 = [] # 저장할 곳
a= 0
avg = 0
while True : 
    print("1. 값추가")
    #print("2. 리스트 출력")
    #print("3. 리스트 합 출력")
    #print("4. 리스트 평균 출력")
    #print("999. 종료")
    select = input("번호 선택 : ")
    if select == '1':
        num = int(input("숫자 입력 : "))
        리스트.append(num)
    elif select =='2' : 
        print(리스트)
    elif select == '3' :
        print(f'{sum(리스트)}')
    elif select == '4':
        
        for item in 리스트 :
           # print(item)
            avg = item + avg
            # 이렇게 하면 초기화가 안된다. 그렇기때문에 전에 했던 것들이 누적이 되서 값이 이상하게 나온것이다. 그냥 모두 초기화를 해줘야한다. 자동적으로 초기화가 되지 않는다.
            print(f"전체 값 : " , avg)
            a += 1
        print(avg/a)
        avg = 0
        a= 0
        print(a)
        print(avg)

    elif select == '999' : 
        print("감사합니다.")
        break
    else :
        print("다시 입력해주세요")
"""

# len을 사용하면 된다 . 길이
# sum은 리스트를 넣으면 싹 더해줌
# 이상함 수정해야됨