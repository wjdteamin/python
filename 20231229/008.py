# 함수, 변수 -> 이름을 가진다 -> 재사용 할라고
a = 80
jumsu = 85

# 성적합계는 220 점이다
# SumOfAllScores = 220      C
# sumOfAllScores = 220      JAVA
# sum_of_all_scores = 220   Python

# 이름은 알아보기 쉽게, 소문자, _ 로 만든다
sum_of_all_scores = 220

# 키워드(예약어)는 사용할수 없다
# 파이썬이 사용하는 단어 ex)True, int 등등

#당신의 이름을 변수에 저장하시오
my_name = "황규민"
nai = 22

# 제 이름은 김기준
print("제 이름은",my_name)

# 나이를 1 증가 시킨다음 "나이는 23이라고 출력"
nai += 1
print("나이는",nai,"살")

# 변수를 적절히 만들어 아래와 같이 출력하시오
# 우리집 강아지 이름은 초코에요
# 초코는 산책을 아주 좋아해요/

dogname = "초코"

print("우리집 강아지 이름은 " + dogname + "에요")
print(dogname + "는 산책을 아주 좋아해요")

# 3,000,000이라는 값을 저장하는 변수를 작성하시오
# 변수를 이용해 아래와 같이 출력하시오
# 급여 : 3,000,000

my_money = 3000000

print("급여 :", my_money)
print("급여 : " +  str(my_money))

# 삼성전자 라는 변수에 현재 주가를 저장하시오
# 주식을 10주 보유하고 있을때 총 평가 금액을 출력하시오
# 총 평가금액 : 78000원

samsung = 78500
고객의주가총액 = samsung * 10
print("총 평가금액 : " + str(고객의주가총액)+"원")