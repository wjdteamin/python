import e005
#from e005 import hello   e005를 쓰기 싫으면 from을 적으면 된다. ->hello()
# from e005 import hello, py 여러개의 함수를 사용하고 싶으면 ,를 사용하면 된다.


e005.hello()

# e005에 파이썬이라고 출력하는 함수를 정의하고 006.py에서 호출하시오

e005.py()


def message():
    print("A")
    print("B")

# 함수는 동시에 실행되지 않는다.(한번에 하나씩 실행)
# 하나가 끝나야 그 다음 코드가 실행된다.

# 병렬 프로그래밍 : 함수를 동시에 실행하는 것   
message()
print("C")
message()


# 서버와 통신하는 코드는 병렬로 돈다.
# 통신하는 동안에 이미 진행이 되서 정보가 없다. 
"""
    await async 공부하기
"""

# 함수는 반드시 인자를 가지고 있어야한다. 만약 인자가 주어지지 않으면 저장된 기능을 실행한다.

