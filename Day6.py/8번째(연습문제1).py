num = []
while True : 
    select = input("1 : 숫자 추가, 2 : 숫자 출력, 3 : 합계, 4 : 값으로 삭제, 999 : 종료 ")
    

    if select == "1" :
        numbers = int(input('숫자 입력 : '))
        num.append(numbers)
        #print(num)
    elif select == "2" : 
         for number in num:
             print(number, end=" ")
             #print(num)
         print()
    elif select == "3" :
        # print(f'합계 : {sum(num)}')
        sum1 = 0
        for x in num :
            sum1 = sum1 + x 
        print(sum1)
    elif select =='4' : 
        val = int(input("삭제 번호 : "))
        if val in num : 
            num.remove(val)
        else :
            print("그런 값 없습니다")
    elif select == '999' : 
        break

# for x in 