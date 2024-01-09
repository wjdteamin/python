# 숫자를 2개 입력받아 다음과 같이 출력하시오

# 예) 3과 8의 합은 11, 곱은 24입니다

input_num1 = int(input("첫번째 숫자를 입력해주세요 : "))
input_num2 = int(input("두번째 숫자를 입력해주세요 : "))

result_plus = input_num1 + input_num2
result_times = input_num1 * input_num2

print(f"{input_num1}과 {input_num2}의 합은 {result_plus}, 곱은 {result_times}입니다")