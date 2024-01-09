numbers = [100,300,500,700]
# 위치를 입력 : 2 -> del numbers[2]

# 값을 입력받아 위치를 찾아서 삭제
value = 500

index = 0 
for item in numbers : 
    if value == item :              #2 
        print(index)
    index = index+1 # if문 안에서는 조건이 맞아요 하기 때문에 밖에서 하는게 맞다. 
# 삭제작업. 내가 알고픈 값 : 2
