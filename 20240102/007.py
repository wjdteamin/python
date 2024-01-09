# 연산
# 산술연산
# +,-,*,/
# 몫 : //, 나머지 : %

print(18/5)
print(18//5)
print(17%5)

x = 15.72
# x의 소수점 이하를 버리고 출력하시오
print(x//1)

a,b = 19,5
# %연산 금지, 나머지를 출력하시오(+,-,*,/,//)


result = a-((a//b)*b)
print(result)

y = 453
# y를 1의 자리에서 버림 : 450

result = y-(y%10)
print(result)

# % 금지
result = y//10*10
print(result)

#숫자를 입력하면 그 숫자 보다 작은 최대의 짝수
# 7 -> 6

input_num = int(input("숫자를 입력하세요 : "))
input_num = input_num - input_num%2
print(input_num)

# 숫자를 입력하면 가장 가까운 7의 배수 출력
# 15 -> 21 21-> 21

input_num = int(input("숫자를 입력하세요 : "))

# if input_num%7 != 0 :     
#     plus_num = 7-(input_num%7)
#     input_num = input_num+ plus_num

a = (7-(input_num % 7))%7
print(input_num+a)