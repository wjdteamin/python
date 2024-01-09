#초를 입력받아 몇분 몇초인지 출력
# 예) 210초라고 입력하면 3분 30초

input_second = int(input("초를 입력해주세요 : "))
second = input_second % 60
minute = input_second // 60

# print(f"{minute}분 {second}초")
