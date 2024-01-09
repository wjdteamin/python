# 75 ,80 ,70 이라는 국어 점수가 있다 -> 집합 타임(sequence)
# list , tuple, dictionary, set
#
test1_score, test2_score,test3_score = 75 , 80, 70

kor=[75,80,70] 

print(type(kor))
# kor의 타입 출력]\

# 조건문, 반복문

#kor 리시트의 원소를 하나씩 꺼내서 item에 담는다
for item in kor : 
    print(item)

# 리시트는 변경가능하고 , 튜블은 변경 불가능
list = [ "사과", "귤", "수박"]
tuple = ( "사과", "귤", "수박")

# 리스트 튜플 출력
for aaa in list : 
    print(list)

print(tuple)