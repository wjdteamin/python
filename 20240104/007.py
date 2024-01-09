#module : 남의 코드를 가져와 기능 확장 < libarary < framwork

import random
print(random.random())

# 1보다 작은 실수 
a = random.random()

# 10보다 작은 실수
# for i in range(5) :
#     b = int(random.random() * 10)
#     print(b)

# 0~10사이의 랜덤 정수 출력
# for i in range(15) :
#     b = int(random.random() * 11)
#     print(b)

# 1~ 10 사이의 랜덤 정수 출력
for i in range(15) :
    b = int(random.random() *10+1)
    print(b)