# 함수 만들기 => 함수 정의 (가급적 구현이라는 말은 하지말자)
def hello():
    print("hello world")
"""
# 함수 호출 
hello()

"""

# def는 함수를 정의해준다.
def py():
    print("파이썬")

# 값이 정해져 있으면 함수가 필요가 없다. 그래서 인자를 사용자가 줘야한다.

# a라는 데이터의 값을 int라고 하는게 좋다고 나타내준다. 
def a(a:int):
    print(a*a)

#square(45)



numbers = [1,5,7]
for num in numbers : 
    print(a(num))
    print()

# a는 값이 None이라고 지정되어서 None이라고 나온다고한다.....함수는 계산이 끝나면 값으로 바뀐다.
    
def sample(a:int):
    print(a)

sample(10)
sample('hello')
# def sample(a:int):에서 int를 사용하는 것은 그냥 권유사항이다. 

# 정수 2개를 인자로 받아 덧셈 후 출력하는 함수를 정의하고 호출 
def hap(a:int |float, b :int| float):
    print(a+b)
hap(3.34,4)

# True | False

def hap2(a:int|float, b:int|float):
    #return 결과 -> 함수를 종료하고 결과로 바꿔라
    return a+b

print(hap2(3,4)) # 직접 출력하거나 변수에 저장하여 출력할 수 있다.

result = hap2(3,4)
print(result)
