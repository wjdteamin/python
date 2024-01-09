
# 분과 초를 입력하면 초를 출력하시오
# 코드에 값이 직접 나타나는 것 : literal
# 5분 10초 -> 310초

input_min = int(input("몇분? : "))
input_second = int(input("몇초? : "))

#상수는 대문자로
SECONDS_PER_MINUTE = 60

print(f"{input_min*60 + input_second}초")