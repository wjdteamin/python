# 두 숫자를 입력받아 큰 수를 가리는 함수

"""
c = 0
def max_numbers(a, b):
    return max(a,b)

num1 = int(input("첫번째 숫자 : "))
num2 = int(input("두번째 숫자 : "))
c = max_numbers(num1, num2)

print(c)
"""

# 같은 경우는? 

"""
def large(a : int, b : int) :
    if a> b:
        return a
    else : 
        return b
"""

# 숫자를 입력받아 절대값을 계산하는 함수

def absolute(a : int):
    if a >= 0:
        return a
    else :
        return -a

b = 324577797979797979
c = absolute(b)
print(c)

# 0인 경우에는? 그냥 자연수에 포함하면 되는거 아님?
# 실수는 ? 그냥 가능 

"""
 def absolute(a : int)
    if a< 0 :
     return -a
    return a 
이렇게 사용이 가능하다.
"""

# 파이썬에서는 이름이 겹치면 덮어쓴다. 자바에서는 에러가 난다. 