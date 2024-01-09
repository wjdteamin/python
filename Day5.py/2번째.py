lang = 'python'
#slicing 가능하다.
print(lang[0])
print(lang[5]) #n

print('a' in lang) #in 

# list는 데이터들의 집합이다. 
# 문자열은 문자들의 집합이다.

print('p' in lang) # 소문자 
print('P' in lang) #대문자

#뒤에서 slicging
print(lang[-1]) #뒤에서할 때는 음수로 한다. 0은 맨 앞에 인덱스로 사용  (확장자를 확인할 경우)

string = '123456789'
# 문자열[시작위치 : 끝위치 + 1]
print(string[1:3])

# 문자열[시작위치 : 끝위치 + 1 : 간격]

print(string[1::5])

# 짝수만 출력
print(string[1::2])
# set은 순서가 없다. 그래서 위의 작업을 못한다. 


jumin = '961011-1021023'
gender = jumin[7]

# 남자인지 여자인지
if gender == '1' : 
    print('남자')
else : 
    print('여자')

# 둘둥의 하나 if문을 한줄로 -> 삼항연산자 (elif를 사용하면 안됨. 복잡해짐.) -> 복잡한 조건 삼항연산은 쓰지말자 -> 스파게티 코드 
# 값 : 조건 
print("남자" if gender == '1' else "여자")
# 식이다. ''으로 묶으면 실행이 안되고 그냥 문자로 인식한다.

# 외계인 코드  : 너무 최적화해서 읽기 어려움
# 스파게티 코드


# gender가 1 또는 3 또는 5면 남자, 2, 4, 6이면 여자
#print("남자") if gender == '1' or   gender == '3'or  gender == '5' else print("여자")

# "남자" if gender in ('1','3','5') else "여자"

# 주민번호로 나이 출력하기 
# 1. 올해의 년도 
# 2. 태어난 년도 
#   주민번호 앞 2자리를 슬라이싱한다.  -> year
#   주민번호 7번째가 '1', '2' -> 19 + year
#   주민번호 7번째가 '3', '4' -> 20 + year
# 3. 올해의 년도 - int(태어난년도)

# 모든 파이썬 파일은 모듈이다. 남이 사용할 수 있다.
import datetime
# 이번년도를 import로 가져온다. 
this_year = datetime.datetime.now().year
print(this_year)



year_birth = jumin[0:2]
#print(year_birth)
if jumin[7] in ('1','2') : 
    year_birth = int('19' + year_birth)
elif jumin[7] in ("3","4") : 
    year_birth = int('20' + year_birth)
else : 
    print('사람입니까? 어떻게...?')
#age = this_year - year_birth
print(f'나이는 {this_year - year_birth}세 입니다')

# 파이썬은 동적타입니다. 가변적으로 바뀐다.