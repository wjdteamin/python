#섭씨를 입력받아 화씨로 출력하시오 (0°C × 9/5) + 32 = 32°F

input_celsius = int(input("섭씨? : "))

fahrenheit =(input_celsius * 9/5) + 32

print("화씨 : " +str(fahrenheit))

#온도와 종류를 입력받으시오
# 예) 온도 : 35 
# 예) 종류 : 섭씨
# 종류가 섭씨면 온도를 화씨로변환, 아니면 섭씨로 변환

# 1. 섭씨면 화씨로, 화씨면 섭씨로 변경하는 프로그램
# 2. 온도 입력 -> 입력 온도가 섭씨? 화씨?
# 3. 섭씨 또는 화씨를 입력받는디 -> kind
# 4. kind가 섭씨면 화씨로 변환

input_tem = int(input("온도? : "))
input_type = input("종류? : ")

if input_type == "섭씨" :
    result = (input_tem * 9/5) + 32
    print(str(result) + "F")
elif input_type == "화씨"  :
    result = 5/9*(input_tem-32)
    print(str(result) + "C")
else :
    print("잘못 입력하였습니다")