# 숫자를 입력받아 1의 자리까지 버리고 출력
# 예) 3512 - 3519 , 369 - 350

input_num = int(input("숫자? : "))

result = input_num//10 *10

print(f"결과 : {result}")

