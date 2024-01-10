# 정수변수를 2개 만들어, 나눗셈 결과를 결과를 출력하시오.
# 예외처리가 필요하면 예외처리하시오.

def divide(a : int,b : int):
        return a / b # 문제는 여기서 생긴다. 

        #return None
 
try : 
    num1 = int(input('첫번째 값 : '))
    num2 = int(input('나눌 값 : '))
    print(divide(num1, num2)) 
except :
      print("안되요")
#print(num1/num2)
# print("안녕") 위의 코드가 문제 생기면 그 밑에 코드는 실행되지 않고 except로 넘어간다. 

# 코드를 작성할 때, 항상 예외를 생각해야한다. 발견하는 것이다. 
    
# 예외처리는 사용하는 사람이 해결하는 게 맞다. 즉, 함수만들때 보통 try를 사용하지 않는다.

# try: except를 함수안에 넣으면 발생하는 문제! 
# 1. 값을 입력할 때 문자를 입력하면 에러가 발생한다. 그럼 2개를 만들어야하나?