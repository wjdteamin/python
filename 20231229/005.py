#파이썬은 타입을 바꿀 수 있고 파이썬이 알아서 바꾸는 경우도 있음

# int, str, float, bool, (list, set, diction)
# 타입을 바꾸는 함수는 타입의 이름과 같다
'3'

print(type(int('3')))

# '3'을 정수로 바꾼 다음 타입을 확인해보자
#int(), type(), print()
print(type(int('3')))

# 6이 나오게 수정

print(3 + int('3'))

# 3+'3.14'를 출력(6.14)
print(3 + float('3.14'))

print('3'+'3')
# '55'
print('5'+str(5))

print('당신은 성인입니까? ' + str(True))