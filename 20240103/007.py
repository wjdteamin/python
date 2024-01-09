username = input('아이디 입력')
nai = input('나이 입력')
print(type(username))
print(type(nai))
# 사용자가 입력받은 값의 타입은 문자열이다
# 개발자가 타입을 바꿔준다
nai = int(nai)
print(type(nai))