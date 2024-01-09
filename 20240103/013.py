# 숫자를 입력받아 3의 배수인지 아닌지 출력하시오
jumsu = int(input("점수? : "))
if jumsu%3  == 0:
    print('3의 배수')
else :
    print("3의 배수 아님")

# 점수를 입력받아 90점이상이면 우수 70점 이상이면 패스 미만이면 낙제라고 출력하시오
if jumsu>= 90 :
    print("우수")
elif jumsu >= 70 : 
    print("패스")
else:
    print("낙제")