# 1년은 몇초인지 출력
year = 1
DAY = 365
HOUR = 24
MINUTE = 60
SECOND = 60

result = DAY * HOUR * MINUTE * SECOND
print(result)

# 45분간 일하고 10분씩 휴식, 전체 근무시간 480분이면 
# 휴식 시간의 합계는 얼마인가

total_time = 480
work_time = 45
rest_time = 10

result = (total_time//(work_time+rest_time))*rest_time

print("휴식시간의 합계는 : "+ str(result))