#함수 : 이름을 가진 코드 덩어리

#print, type, int, float, str

print(type({"irum" : "홍길동", "nai" : 20}))

a = {"irum" : "홍길동", "nai" : 20}

# 5+3의 타입을 확인하시오
print(type(5+3))

#max(num1,num2) : 최대값 구하기
result_max = max(3,4)
print(result_max)

# 10,20 중에 작은 값을 출력하시오
result_min = min(10,20)
print(result_min)

# sum (iterable  <- type 맞지않음
print(sum([10,20]))

# a = [10,20]
# print(type(a))

# 3,7 , 10 중에 가장 큰 값을 출력하시오
result_max = max(3,7,10)
print(result_max)

# 3,7 중에 큰 값과 10의 합계, 즉 17을 계산해 출력하시오
result_max = max(3,7)
print(result_max+10)
