#몇일인지 입력받아 몇개월 며칠인지 출력
# 333일 - > 11개월 3일

input_day = int(input("몇일? : "))

print(f'{input_day//30}개월 {input_day%30}일')