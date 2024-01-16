# import hh
# from hh import a
import random
from random import random
import datetime as d



print(random())

print(d.datetime.now())
# 데이터 안에 클래스가 있고, 클래스 안에 함수가 있다. d.datetime.now() 객체

print(d.datetime.now().date().weekday())
# d는 모듈로 가져온 것이다. import는 모듈을 다 가지고 온다. 

# d는 modue, datetime은 클래스, now()는 메소드
# now()란 현재시각 datetime을 리턴한다. -> now()를 통해 datetime을 리턴한다. 그리고나서 .을 이용해서 메소드를 부를 수 있다.
# 메소드를 계속 불러온다. -> d.datetime.now().date()

# 전체를 가져와서 .을 이용해서 쪼개고 쪼개서 필요한 부분만 출력할 수 있게 해준다. -> d.datetime.now().date().weekday()


# scope : 변수의 사용범위. 파이썬은 함수 스코프 
x =10
def func1():
    x=30
    return x 

x = func1()
print("함수 밖에서 : ", x)