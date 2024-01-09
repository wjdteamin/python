# 자연수를 입력받아 그 숫자보다 작거나 같은 최대의 7의 배수
#  17 -> 14 21->21

input_num = int(input("숫자? : "))

result = input_num//7*7

print(f"결과 : {result}")

# 자연수를 입력받아 그 숫자보다 작거나 같은 최대의 7의 배수
#  17 -> 14 21->14

result = (input_num-1)//7*7

print(f"결과 : {result}")