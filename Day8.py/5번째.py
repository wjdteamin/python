# for문 아이템 in 집합

# hello를 for를 이용해 3번 출력하시오. 
for x in range(2):
    print('hello')

# range -> 범위를 설정해줘서 사용이 가능하다. 집합대신
    
# for를 이용해서 0~10사이의 짝수 
# for x in range(11):
#     if x % 2 == 0 :
#         print(x)

# 순서를 바꾸는 것을 if, for을 사용해야한다.

# 1부터 10의 합계를 출력 
#for : 0
#if : x 
# r = 0 
# for x in range(1,11):
#      if x > r :
#          r=x
# r = (r*(r+1))/2
# print(r)

result = 0  # reslut= 0이 for에 있으면 계속 초기화가 된다. 그래서 안됨 
for x in range(1,11) : 
    result = result + x

print(result)

print()
# 1~ 100 사이의 3과 5의 공배수를 출력 
for x in range(1, 101) :
    if x % 35 == 0:
        print(x)
# if i%5==0 and i%7 == 0: 
    
print()
# 1~ 100사이의 5의 배수와 7의 배수를 출력, 단 공배수는 제외
for x in range(1, 50) : 
    if (x%11==0 or x%5 == 0) and x% 55!=0:
        print(x) 
#     if x%5==0 or x%7 == 0 and x% 35!=0: 이렇게 하면 and에서 35와 70이 걸러진다. 하지만, 5에서 다시 포함되서 출력된다. 

print() 
for x in range(1, 50) : 
    if x%5==0 or x%7 == 0 :
        if x% 35==0:
            continue
        print(x) 
#     if x%5==0 or x%7 == 0 and x% 35!=0: 이렇게 하면 and에서 35와 70이 걸러진다. 하지만, 5에서 다시 포함되서 출력된다. 

print()
# for x in range(1, 101) : 
#     if x% 5 ==0 and x%7!=0 :
#         print(x)
#     if x% 7 == 0 and x% 5!= 0:
#         print(x)

for x in range(1, 101) : 
     if x% 5 ==0 or x%7==0 :
         print(x, end =" ")
