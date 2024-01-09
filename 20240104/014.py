# 길이를 입력받아 센티미터 또는 인치로 변환해 출력한다
# 길이가 양수인 경우 인치로 변환,
# 음수인 경우 센티미터로 변환

input_num = int(input("길이? : "))

if input_num > 0 :
    print(f"{input_num/2.54}인치")
elif input_num == 0 :
    print("0")
else : 
    print(f"{input_num*2.54}Cm")

# scope : 변수를 사용할수 있는 범위
# 블록이 스코프를 생성하는 언어 : 자바
# 함수가 스코프를 생성하는 언어 : 파이썬.