# 변수의 이름이 겹치면 덮어쓴다 -> 겹치면 안된다
# 변수의 이름은 쉬워야한다

# = : 같다는 뜻이 아니다. 오른쪽에서 왼쪽으로 대입
a = 10
a = 20
a = a + 1

# 올해의 년도를 저장하는 변수를 정의하시오

this_year = 2024

# 현재 살고 있는 도시를 저장하는 변수를 정의 하시오
living_city = '인천'
# 서울의 위도는 37.33, 경도는 127.00이다
seoul_latitude =  37.33
seoul_longitude =  127.00

# 서울의 위도와 경도를 저장하고 위도를  1증가해 출력
print("위도 : " + str(seoul_latitude+1) +", 경도 : " +str(seoul_longitude))
