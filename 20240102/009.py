# 숫자를 2개 입력받아 큰수와 작은수를 출력하시오
# 예 : 5와 8중 큰수는 8, 작은수는 5입니다.

input_num1 = int(input("첫번째 숫자를 입력해주세요 : "))
input_num2 = int(input("두번째 숫자를 입력해주세요 : "))

high_num = max(input_num1,input_num2)
low_num = min(input_num1,input_num2)

print(f"{input_num1}와 {input_num2}중 큰수는 {high_num}, 작은수는 {low_num}입니다")