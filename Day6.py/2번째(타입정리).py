# 숫자 타입 -> 타입마다 사용할 수 있는 연산, 함수가 다르다.
# 산술연산 : +, -, *, /, //, %
num,PI = 10, 3.14
print(f'더하기 {num + PI}, 빼기 {num - PI}, 곱하기 {num * PI}, 나누기 {num / PI}')
print(f'빼기 {num - PI}')
print(f'곱하기 {num * PI}')
print(f'나누기 {num / PI}') 
# f-문자열을 사용하는 것은 편리하기 때문이다. f를 사용하지 않으면 변수는 그냥 문자로 인식해서 그대로 출려된다. 

pin = 3 
print(f'몫 {num // pin}')
print(f'나머지 {num % pin}')

print(abs(-100))
print(abs(100))
print(abs(-24))

# 함수 : 이름을 가진 기능 -> 재사용 
# 처음부터 사용할 수 있는 함수 -> 내장함수 (import X) -> 기본타입과 비슷한 경우다.
# 절대값을 사용할 수 있게 해주는 함수? abs 

print(abs(1000-100))
# abs()만 실행하면 에러나타난다. 심부름값을 줘야한다. 그게 인자다!!!! 


# 원시타입, 내장함수 <-> import
# 개발자는 값을 검증

#str 타입
str1 = '10'
str2 = '3.14'
str3 = "홀짝홀짝홀짝홀짝"

# 문자열 연산
print(str1 + str2)  # 연결
print(str1 * 10)    # 반복
# 인덱스 연산 (순서로 접근한다.) -> 시퀀스(sequence)와 동일 
print(str3[0]) #원래는 sequence에서 사용하지만, 문자열에서도 사용이 가능하다.
print(str3[5])

# 슬라이싱(slicing) 연산 -> 시퀸스와 동일
print(str3[0:3]) # 홀짝홀 (그전까지만 출력된다.)
str4 = "12345678"
print(str4[3:]) #45678
print(str4[0:3]) #123
print(str4[::2])


str5 = "0123456789"
# 홀수만 출력 -> 13579
# 3의 배수만 출력 ->0369
print(str5[1::2])
print(str5[0::3])

# 내장함수 : len (길이)
print(len(['hello']))

# 길이를 알려면 집합이여야 한다. 언어마다 다르다.

# 문자열은 변경불가능(immutable(불변) <-> mutable(변하기 쉬운)), sequence
str6 = 'hello'
list6 = ['h','e','l','l','o']
#str6[0] ='z' 에러난다.
list6[0]= 'z'
print(list6)

# 언어마다 정의가 다르다. 
# 참조변수를 한번 봐야겠다.