# 점수를 입력받아 70~90점 이면 추천대상 아니면 대상아님
input_num = int(input("점수? : "))

if input_num >= 70 and input_num <= 90 :
    print("추천대상")
else : 
    print("대상아님")