# 파이썬 타입 : int, float, str, bool, tuple, list, dict, set
# 파이썬으로 타입 자체를 만들 수 있다. -> 사용자 정의 타입 : class

#c언어는 c언어로 만들었다.

# 타입은 필요한 데이터를 저장하고 연산을 수행할 수 있다.

"""
    데이터 
    기능 -> 함수

    함수를 가지고 기능을 재사용했는데, 정확하게 의미를 모르면 쓰기가 힘들다.
    그래서 같이 다녀야 할 것들을 묶어서 보낸다. -> 관련된 데이터와 함수를 묶자 -> class

    여행 갈 때, 옷도 챙기고, 양말도 챙기고, 속옷도 챙기고 많은 것들을 챙길 때, 캐리어에 담는다. 그 가방 역할을 하는게 class다.

    파이썬은 타입이 8개밖에 없다. 근데 class를 만들면 늘어난다. -> 내가 만든 typte인 클래스의 변수를 object(객체)라고 한다.
    -> 객체에는 데이터와 함수가 들어있다. 

    클래스 -> 설계도 
    그 클래스의 변수를 객체라고 한다. 

    예) 붕어빵를 예로 들면
    클래스 -> 붕어빵 틀
    붕어빵 하나하나를 객체라고한다. 

    딕셔너리는 틀이 없다. 한번만 사용할 거면 사용한다.

"""
# 파이썬의 모든 타입은 클래스다. 
# 파이썬의 모든 변수는 객체다. 
# 객체에 소속된 함수를 메소드라고 한다. 

# is는 물어보는 것.
str = 'hello'
print(type(str))

print(len(str))