#1부터 10까지의 합계 : 55

i = 0
for x in range(1,11):
    i += x

print(i)

# s = 0 
# for x in range(1,11) : 
#     if x > s :
#         s = x 
#         print(s)
# c = (s*(s+1))/2
# print(c)

print()
# # 1에서 10까지의 3의 배수 출력 -> 3,6,9
# for item in range(1,11) :
#     if item % 3 != 0 :
#         continue    # skip 밑에 코드를 쓰지 무시하고 올라간다.
#     print(item)


sum1 = 0
# 1 ~ 10 사이의 3의 배수의 합계 -> 3 6 9 -> 18
for item in range(1, 11) :
    if item %3 == 0:
        sum1 += item
        #print(item)

print(sum1)

sum2 = 0
for item in range(1, 11) :
    if item %3 != 0:
        continue
    sum2 += item
        #print(item)

print(sum2)
