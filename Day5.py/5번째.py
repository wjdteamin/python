"""
list1 = [1,3,5]

# 10 in list1 : 결과가 참거짓(10이 list1에 있니?)

# list1의 원소를 하나씩 꺼내 item에 담는 반복문 
for item in list1 :
    print(item)

# 숫자를 줘야한다.
index = 0 
while  index <3 : 
    print(list1[index])
    index +=1
# 강제종료 ctrl + c 

"""

# True는 무한 반복이다.....break가 있으면 종료됨
# break : 반복문을 중단한다.

while True : 
    a = int(input('값을 입력하세요(999면 종료)'))
    if a == 999:
        print('이용해주셔서 감사합니다')
        break
    print(f'입력한 값 : {a}')


