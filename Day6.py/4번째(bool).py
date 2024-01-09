# bool
b1, b2, b3, b4 = True, True, True, False
# and : 모두 다 참이어야 한다.
# or : 하나만 참이면 된다.

print(b1 and b2 and b3) # True
print(b1 and b2 and b4) # False
print(b1 or b2 or b4)   # True

# 두 개의 코드중 더 효과적인 코드는 print(b4 and b2 and b3)다. 왜냐하면 다 보는 것이 아닌 중간만 보면 되니까!
print(b1 and b2 and b4)
print(b4 and b2 and b3)

# 끝까지 보지 않아도 알 수 있다.
print(b1 or b2 or b4)

# and와 or 둘 다 있으면 and가 먼저 계산된다. 

nai = 30
gender = "남자"
city = '인천'
# 나이가 20이상이고 성별은 남자
print()
print(nai>=20 and gender == "남자")

# 하나의 조건(나이가 20이상이고 성별은 남자인 사람) 또는 인천에 사는 사람(하나의 조건)

print((nai>=20 and gender == "남자" ) or city =='인천')


